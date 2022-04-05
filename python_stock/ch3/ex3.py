# 주가 일간 변동률 히스토그램
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf
sec = pdr.get_data_yahoo('005930.ks', start='2022-04-04')

print(sec['Close'])

sec_dpc = (sec['Close'] - sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
sec_dpc.iloc[0] = 0
plt.hist(sec_dpc, bins=18)
plt.grid(True)
plt.show()

print(sec_dpc.describe())

sec_dpc_cs = sec_dpc.cumsum()
print(sec_dpc_cs)