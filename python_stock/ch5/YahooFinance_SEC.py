from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt



df = pdr.get_data_yahoo('005930.KS', '2022-04-14')

plt.figure(figsize=(9,6))
plt.subplot(2,1,1)
plt.title('Samsung Electronics (Yahoo Finance)')
plt.plot(df.index, df['Close'], 'c', label='Close')
plt.plot(df.index, df['Adj Close'], 'b--', label='Adj Close')
plt.legend(loc='best')
plt.subplot(2,1,2)
plt.bar(df.index, df['Volume'], color='g', label='Volume')
plt.legend(loc='best')
plt.show()

# 삼성전자 종가, 수정종가, 거래량