from pandas_datareader import data as pdr
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

dow = pdr.get_data_yahoo('^DJI', '2020-01-04')
kospi = pdr.get_data_yahoo('^KS11', '2020-01-04')


df = pd.DataFrame({'DOW': dow['Close'], 'KOSPI': kospi['Close']})
print(df)


plt.scatter(df['DOW'], df['KOSPI'], marker='.')


df2 = df.fillna(method='bfill')
print(df2)