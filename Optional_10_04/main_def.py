# This module backtests strategy based on
# clusterd alphas in Problem 2, using the backtest system in Problem 1
# First draft 2016/10/6
# This draft 2016/10/6

from setalphas import SetAlphas
from k_mean_cluster import KmeanCluster
from datahandler2 import DataHandler2
from record import Record
from test_fan import TestFan
from portfolio import Portfolio
from analyzer import Analyzer


# Stock data is the same as is uesd in Problem 2
# However, it's divided into two group, for training and testing
data = DataHandler2('stock_train.csv').data
record = Record()
SetAlphas(data, record)
k_means = KmeanCluster(record, data.returni)

data_result = DataHandler2('stock_test.csv').data
record_result = Record()
SetAlphas(data_result, record_result)

record_trade = Portfolio()
TestFan(k_means, record_result, data_result, record_trade, 1000000)

Analyzer(data_result.time_, record_trade, data_result)
