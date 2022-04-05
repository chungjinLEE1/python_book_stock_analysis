from pandas_datareader import data as pdr
import yfinance as yf
print(yf.pdr_override())

sec = pdr.get_data_yahoo('005930.KS', start='2022-04-03')
msft = pdr.get_data_yahoo('MSFT', start='2022-04-03')

print(sec.head(10))
tmp_msft = msft.drop(columns='Volume')
print(tmp_msft.tail())


print(sec.index)
# 데이터프레임의 칼럼들에 대한 정보 
print(sec.columns)