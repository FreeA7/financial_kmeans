# This module receives and processes the bar data
# First draft 2016/10/3
# This draft 2016/10/6


import pandas as pd
import datetime


# The sample data is a stock in HS300 taken randomly from Tushare 
class DataHandler2(object):

    def __init__(self, path):
        self.path = path
        self.data = pd.read_csv(self.path)
        self.data.returni = []
        for i in range(1, len(self.data)):
            self.data.returni.append(
                (self.data.close[i] - self.data.close[i - 1]) / self.data.close[i - 1])
