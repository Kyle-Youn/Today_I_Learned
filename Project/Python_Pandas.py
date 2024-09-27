import pandas as pd

# 데이터 프레임 생성
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32]}

df = pd.DataFrame(data)

# 데이터 프레임 출력
print(df)

# 데이터 통계 정보
print(df.describe())

# 특정 조건 필터링 (Age가 30 이상인 사람들)
print(df[df['Age'] >= 30])
