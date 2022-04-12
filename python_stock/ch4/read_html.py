import pandas as pd
krx_list = pd.read_html('C:/#dev_chungjin/Excel_file/cooperation_list.xlsm')
# print(krx_list[0])



krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06d}'.format)
print(krx_list[0])


