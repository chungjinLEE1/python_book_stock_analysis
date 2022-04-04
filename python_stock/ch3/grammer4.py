import pandas as pd

print("## 1. 딕셔너리를 이용한 데이터 프레임 생성. ")
df = pd.DataFrame({'KOSPI': [1915, 1961, 2026, 2467, 2041], 'KOSDAQ': [542, 582, 631, 798, 675]})
print(df)

df2 = pd.DataFrame({'KOSPI': [1915, 1961, 2026, 2467, 2041], 'KOSDAQ': [542, 582, 631, 798, 675]}, index=[2014, 2015, 2016, 2017, 2018])
print(df2)

print(df2.describe())
print(df.describe())


print("## 1.1. df.info")
print(df.info())


print("## 2. 시리즈를 이용한 데이터 프레임 생성")
kospi = pd.Series([1915, 1961, 2026, 2467, 2041], index=[2014, 2015, 2016, 2017, 2018], name="KOSPI")
print(kospi)

kosdaq = pd.Series([542, 682, 631, 798, 675], index=[2014, 2015, 2016, 2017, 2018], name="KOSDAQ")
print(kosdaq)

df3 = pd.DataFrame({kospi.name : kospi, kosdaq.name : kosdaq})
print(df3)


print("## 3. 리스트를 이용한 데이터 프레임 생성")
columns = ['KOSPI', 'KOSDAQ']
index = [2014, 2015, 2016, 2017, 2018]
rows = []
rows.append([1915, 542])
rows.append([1961, 682])
rows.append([2026, 631])
rows.append([2467, 798])
rows.append([2041, 675])

df4 = pd.DataFrame(rows, columns = columns, index= index)
print(df4)

print("## 4. 데이터프레임 순회 처리")
for i in df.index:
    print(i, df['KOSPI'][i], df['KOSDAQ'][i])

for row in df.itertuples(name='KRX'):
    print(row)


print("#### itertuples()")
for row in df4.itertuples():
    print(row[0], row[1], row[2])


print("#### iterrows()")
for idx, row in df4.iterrows():
    print(idx, row[0], row[1])