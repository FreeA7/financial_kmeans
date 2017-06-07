# This module downloads stock data from Tushare
# First draft 2016/10/5
# This draft 2016/10/6


import random
import tushare as ts

a = random.randint(0, 300)
weight = ts.get_hs300s()
weight_random = weight[a:a + 1]
print(weight_random.code)
data = ts.get_hist_data(str(weight_random.code[a]))
data.to_csv('stock_smaple.csv')
