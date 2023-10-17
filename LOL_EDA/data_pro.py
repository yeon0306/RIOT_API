import pandas as pd
import numpy

# DataFrame을 불러오기
df = pd.read_pickle("0825_game_data.pkl")

# 유저 ID 목록 생성
ids = set()
for id, _, _ in df.index:
    ids.add(id)
ids = sorted(ids)

# 각 유저의 플래티넘 티어 이상의 유저 수 계산
platinum_or_higher_users = 0
for id in ids:
    tier_data_id = df.loc[(id, slice(None), 'tier')].values
    tier_data_1d = list(np.concatenate(tier_data_id))

    # 플래티넘 티어 이상의 티어 코드 목록
    target_tiers = ["P", "E", "D", "M", "R", "C"]

    # 유저의 티어 데이터에 플래티넘 티어 이상이 있는 경우
    if any(tier in target_tiers for tier in tier_data_1d):
        platinum_or_higher_users += 1

# 결과 출력
print(f'플래티넘 티어 이상의 유저 수: {platinum_or_higher_users}')