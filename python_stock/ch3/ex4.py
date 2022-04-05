from pandas_datareader import data as pdr
import yfinance as yf

sec = pdr.get_data_yahoo('005930.KS', start='2020-01-01')
sec_pdc = (sec['Close'] - sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
sec_pdc.iloc[0] = 0 # 일간 변동률의 첫 번째 값인 NaN을 0으로 변경한다.
sec_pdc_cs = sec_pdc.cumsum() # 일간 변동률의 누적값을 구한다.


msft = pdr.get_data_yahoo('MSFT', start='2020-01-01')
msft_dpc = (msft['Close'] / msft['Close'].shift(1) -1) * 100
msft_dpc.iloc[0] = 0
msft_dpc_cs = msft_dpc.cumsum()


import matplotlib.pyplot as plt
plt.plot(sec.index, sec_pdc_cs, 'b', label='Samsung Electronics')
plt.plot(msft.index, msft_dpc_cs, 'r--', label='Microsoft')
plt.ylabel('Change %')
plt.grid(True)
plt.legend(loc='best')
plt.show()