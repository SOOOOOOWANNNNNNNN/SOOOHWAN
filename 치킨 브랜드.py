import streamlit as st
import pandas as pd
import time

# --- 페이지 설정 ---
# 페이지 제목, 아이콘, 레이아웃을 설정합니다.
st.set_page_config(
    page_title="치킨 브랜드 분석",
    page_icon="🍗",
    layout="wide"
)

# --- 제목 및 설명 ---
st.title("🍗 대한민국 치킨 브랜드 매출 및 이익 분석")
st.write("국내 주요 치킨 프랜차이즈의 2022년 기준 실적을 비교 분석합니다. (데이터: 공시자료 기반)")

# --- 데이터 생성 (Pandas DataFrame) ---
# 실제 공시자료를 기반으로 데이터를 구성합니다.
data = {
    '순위': [1, 2, 3, 4, 5],
    '브랜드': ['교촌치킨', 'BHC', 'BBQ', '굽네치킨', '푸라닭'],
    '매출액(억 원)': [5176, 5075, 4188, 2344, 1903],
    '영업이익(억 원)': [89, 1418, 641, 175, 173],
    '대표 메뉴': ['허니콤보', '뿌링클', '황금올리브', '고추바사삭', '블랙알리오','장각구이']
}
df = pd.DataFrame(data)

# 영업이익률 컬럼 추가 (데이터를 더 풍부하게 만듭니다)
df['영업이익률(%)'] = round((df['영업이익(억 원)'] / df['매출액(억 원)']) * 100, 2)

# --- 데이터 시각화 ---
st.subheader("📈 브랜드별 실적 비교표")

# st.dataframe을 사용하여 인터랙티브한 표를 표시합니다.
# use_container_width=True로 설정하여 표를 페이지 너비에 맞춥니다.
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True, # 인덱스 열 숨기기
    column_config={ # 컬럼별 세부 설정
        "순위": st.column_config.NumberColumn(
            "순위",
            format="%d위"
        ),
        "매출액(억 원)": st.column_config.ProgressColumn(
            "매출액(억 원)",
            help="브랜드별 매출액입니다.",
            format="%,d억 원",
            min_value=0,
            max_value=int(df['매출액(억 원)'].max()),
        ),
        "영업이익(억 원)": st.column_config.BarChartColumn(
            "영업이익(억 원) 📊",
            y_min=0,
            y_max=int(df['영업이익(억 원)'].max()),
        ),
        "영업이익률(%)": st.column_config.NumberColumn(
            "영업이익률(%)",
            format="%.2f %%"
        )
    }
)

st.markdown("---")

# --- 추가 정보 및 재미 요소 ---
st.subheader("💡 재미로 보는 분석")
col1, col2 = st.columns(2)

# 영업이익률이 가장 높은 브랜드를 찾습니다.
top_profit_margin_brand = df.loc[df['영업이익률(%)'].idxmax()]

with col1:
    st.info(f"""
    **영업이익률 챔피언은?**

    **{top_profit_margin_brand['브랜드']}**이(가) **{top_profit_margin_brand['영업이익률(%)']}%**로
    가장 높은 영업이익률을 기록했습니다.
    """)

with col2:
    # 버튼을 누르면 닭다리가 날리는 효과를 줍니다.
    if st.button("🎉 축하! 치킨 파티! 🎉"):
        st.balloons() # 풍선 효과
        time.sleep(1) # 1초 대기
        st.snow() # 눈 효과 (기본)
        time.sleep(1) # 1초 대기
        st.success("치킨 닭다리가 하늘에서 내립니다!")
        st.snow(emoji="🍗") # 닭다리 효과!

st.caption("버튼을 눌러보세요!")
