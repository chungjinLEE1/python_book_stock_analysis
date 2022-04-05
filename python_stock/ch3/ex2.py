from pandas_datareader import data as pdr
import yfinance as yf

sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')


import matplotlib.pyplot as plt

plt.plot(sec.index, sec.Close, 'b', label='Samsung Electronics')
plt.plot(msft.index, msft.Close, 'r--', label='Microsoft')
plt.legend(loc='best')
plt.show()


print(type(sec['Close']))

print(sec['Close'])

print(sec['Close'].shift(1))


print("# 일간 변동률")
sec_dpc = (sec['Close'] / sec['Close'].shift(1) - 1) * 100
print(sec_dpc.head())

# 일간 변동률
sec_dpc.iloc[0] = 0
print(sec_dpc.head())