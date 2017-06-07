# This module receives and processes the bar data
# First draft 2016/10/2
# This draft 2016/10/6


import pandas as pd
import datetime


class DataHandler(object):

    def __init__(self, path):
        self.path = path
        self.data = pd.read_csv(self.path)
        self.open_price = self.data.open
        self.close_price = self.data.close
        self.high_price = self.data.high
        self.low_price = self.data.low
        self.trade_volume = self.data.volume
        #self.trade_value = self.data.value
        self.time_ = []

# Change the date format for analysing in analyzer module
        for i in range(len(self.data)):
            self.time_.append(datetime.datetime.strptime(
                self.data.date[i] + ' ' + self.data.time[i], '%Y/%m/%d %H:%M'))
