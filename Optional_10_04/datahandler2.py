# This module receives and processes the bar data
# First draft 2016/10/2
# This draft 2016/10/6

import pandas as pd
import datetime


class DataHandler2(object):

    def __init__(self, path):
        self.path = path
        self.data = pd.read_csv(self.path)
        self.data.returni = []
        self.data.time_ = []
        for i in range(1, len(self.data)):
            self.data.returni.append(
                (self.data.close[i] - self.data.close[i - 1]) / self.data.close[i - 1])

        for j in range(len(self.data)):
            self.data.time_.append(datetime.datetime.strptime(
                self.data.date[j], '%Y/%m/%d'))
