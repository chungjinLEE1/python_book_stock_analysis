import pandas as pd

s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0]) # 리스트로 시리즈 생성
print(s)


# 시리즈의 인덱스 변경
print("1. 시리즈의 인덱스 변경")
s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8])
s.index.name = 'MY_IDX' # 인덱스명 설정
print(s)

print("2. 시리즈명 설정")
s.name = 'MY_SERIES' # 시리즈명 설정
print(s)

print("3. 데이터 추가")
s[5.9] = 5.5
print(s)


ser = pd.Series([6.7, 4.2], index=[6.8, 8.0]) # ser 시리즈를 생성
s = s.append(ser)
print(s)

# 데이터 인덱싱.
print("4. 데이터 인덱싱")
print(s.index[-1])
print(s.values[-1])

print(s.loc[8.0])
print(s.iloc[-1])


print(s.values[:])
print(s.iloc[:])

# 데이터 삭제
print("5. 데이터 삭제")
print(s.drop(8.0))

# 시리즈 정보보기.
print("6. 시리즈 정보보기")
print(s.describe())