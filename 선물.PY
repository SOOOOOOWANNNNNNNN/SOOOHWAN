import random
import time

def gift_lottery(participants, gifts):
    """
    참여자 리스트와 선물 리스트를 받아서 랜덤으로 매칭해주는 함수입니다.
    """
    # 1. 리스트 복사 (원본 유지를 위해)
    participants_list = participants[:]
    gifts_list = gifts[:]

    # 2. 참여자 수와 선물 수가 맞는지 확인
    if len(participants_list) != len(gifts_list):
        print("⚠️ 오류: 참여자 수와 선물 수가 다릅니다!")
        print(f"참여자: {len(participants_list)}명, 선물: {len(gifts_list)}개")
        return

    print("🎉 선물 추첨을 시작합니다! 두구두구두구... 🎉\n")
    time.sleep(1) # 긴장감을 위해 1초 대기

    # 3. 리스트를 랜덤하게 섞기 (가장 중요한 부분!)
    random.shuffle(participants_list)
    random.shuffle(gifts_list)

    # 4. 섞인 리스트를 순서대로 매칭하여 결과 출력
    results = {}
    for i in range(len(participants_list)):
        participant = participants_list[i]
        gift = gifts_list[i]
        results[participant] = gift
        print(f"✨ {participant}님은 -> [{gift}] 당첨! 축하합니다!")
        time.sleep(0.5) # 발표하는 느낌으로 0.5초씩 대기

    print("\n🎁 모든 추첨이 완료되었습니다! 모두 마음에 드시나요? 🎁")
    return results

# ==========================================
# 실행 예시 (여기 있는 내용을 마음껏 바꿔보세요!)
# ==========================================

# 참여할 친구들 이름
my_friends = ["지수", "제니", "로제", "리사", "철수", "영희"]

# 준비된 선물 목록
my_gifts


