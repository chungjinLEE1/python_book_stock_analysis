import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf

dow = pdr.get_data_yahoo('^DJI', '2020-01-01')
kospi = pdr.get_data_yahoo('^KS11', '2020-01-01')

df = pd.DataFrame({'DOW': dow['Close'], 'KOSPI': kospi['Close']})
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')

import matplotlib.pyplot as plt
plt.figure(figsize=(7, 7))
plt.scatter(df['DOW'], df['KOSPI'], marker='.')
plt.xlabel('Dow Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show()