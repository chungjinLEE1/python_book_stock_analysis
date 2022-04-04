# 시리즈 출력하기 
import pandas as pd
s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0, 5.5, 6.7, 4.2])  # 시리즈 생성
print(s)
# s.index = s.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8, 5.9, 6.8, 8.0])  # 시리즈 인덱스
# print(s.index)

# 변경
s.index.name = 'MY_IDX'  # 시리즈 인덱스명 설정
s.name = 'MY_SERIES' # 시리즈 이름 설정

import matplotlib.pyplot as plt
plt.title("ELLIOTT_WAVE")
plt.plot(s, 'bs--') # 시리즈를 bs-- 형태로 출력
plt.xticks(s.index) # x축의 눈금값을 s 시리즈의 인덱스 값으로 설정
plt.yticks(s.values) # y축의 눈금값을 s 시리즈의 데이터값으로 설정
plt.grid(True)
plt.show()