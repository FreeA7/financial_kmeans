# This module sets various alphas based on pseudo-algo given in 101 formulic alphas
# First draft 2016/10/3
# This draft 2016/10/6


import pandas as pd
import numpy as np

# Alpha 6
# Formula: (-1*correlation(open, volume, 10))
def setalpha_6(data, record):

    range_max = len(data.date) - 9

    for i in range(0, range_max):
        record.alpha1.append(-np.corrcoef(
            data.open[i:i + 9], data.volume[i:i + 9])[1, 0])
    record.alpha1 = np.array(record.alpha1[3:-9])

# Alpha 23
# Formula: (((sum(high, 20)/20 < high) ? (-1*delta(high,2)):0)
def setalpha_23(data, record):
    high_boolean = []
    range_max = len(data.date) - 19

    for i in range(0, range_max):

        high_boolean.append(
            (sum(data.high[i:i + 19]) / 20) < data.high[i + 19])

    range_max = len(high_boolean)

    for j in range(2, range_max):

        if high_boolean[j]:
            record.alpha2.append(-(data.high[j] -
                                   data.high[j - 2]))
        else:
            record.alpha2.append(0)
    record.alpha2 = np.array(record.alpha2)

# Aplha_53
# Formula: (-1 * delta(((close - low) - (high - close)) / (close - low),9))
def setalpha_53(data, record):
    value = (((data.close - data.low) - (data.high - data.close)) /
             (data.close - data.low + 0.001))
    range_max = len(value) - 9

    for i in range(0, range_max):
        record.alpha3.append(value[i + 9] - value[i])
    record.alpha3 = np.array(record.alpha3[3:-9])


# Alpha_54
# Formula: ((-1 * ((low - close) * (open^5))) / ((low - high) * (close^5)))
def setalpha_54(data, record):
    numerator = np.array((data.low - data.close) * np.power(data.open, 5))
    denominator = np.array(
        ((data.low - data.high) * np.power(data.close, 5)) + 0.001)
    record.alpha4 = - numerator / denominator
    record.alpha4 = np.array(record.alpha4[3:-18])


# Alpha_101
# Formula: ((close - open) / ((high - low) + .001)
def setalpha_101(data, record):
    numerator = np.array((data.close - data.open))
    denominator = np.array(((data.high - data.low) + 0.001))
    record.alpha5 = numerator / denominator
    record.alpha5 = np.array(record.alpha5[3:-18])


class SetAlphas(object):

    def __init__(self, data, record):
        self.data = data
        self.record = record

        setalpha_6(self.data, self.record)
        setalpha_23(self.data, self.record)
        setalpha_53(self.data, self.record)
        setalpha_54(self.data, self.record)
        setalpha_101(self.data, self.record)
