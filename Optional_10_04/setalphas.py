# This module sets various alphas based on pseudo-algo given in 101 formulic alphas
# First draft 2016/10/3
# This draft 2016/10/6


import pandas as pd
import numpy as np

# Alpha 6
# Formula: (-1*correlation(open, volume, 10))
def setalpha_6(data, record):

    for i in range(9, len(data.date)):
        record.alpha1.append(-np.corrcoef(
            data.open[i - 9:i], data.volume[i - 9:i])[1, 0])

    record.alpha1 = np.array(record.alpha1[10:])

# Alpha 23
# Formula: (((sum(high, 20)/20 < high) ? (-1*delta(high,2)):0)
def setalpha_23(data, record):
    high_boolean = []

    for i in range(19, len(data.date)):

        high_boolean.append((sum(data.high[i - 19:i]) / 20) < data.high[i])

    range_max = len(high_boolean)

    for j in range(range_max):

        if high_boolean[j]:
            record.alpha2.append(-(data.high[19 + j] -
                                   data.high[19 + j - 2]))
        else:
            record.alpha2.append(0)

    record.alpha2 = np.array(record.alpha2)

# Aplha_53
# Formula: (-1 * delta(((close - low) - (high - close)) / (close - low),9))
def setalpha_53(data, record):
    value = (((data.close - data.low) - (data.high - data.close)) /
             (data.close - data.low + 0.001))

    for i in range(9, len(data.date)):
        record.alpha3.append(value[i] - value[i - 9])

    record.alpha3 = np.array(record.alpha3[10:])


# Alpha_54
# Formula: ((-1 * ((low - close) * (open^5))) / ((low - high) * (close^5)))
def setalpha_54(data, record):
    numerator = np.array((data.low - data.close) * np.power(data.open, 5))
    denominator = np.array(
        ((data.low - data.high) * np.power(data.close, 5)) + 0.001)
    record.alpha4 = - numerator / denominator
    record.alpha4 = np.array(record.alpha4[19:])


# Alpha_101
# Formula: ((close - open) / ((high - low) + .001)
def setalpha_101(data, record):
    numerator = np.array((data.close - data.open))
    denominator = np.array(((data.high - data.low) + 0.001))
    record.alpha5 = numerator / denominator
    record.alpha5 = np.array(record.alpha5[19:])


class SetAlphas(object):

    def __init__(self, data, record):
        self.data = data
        self.record = record

        setalpha_6(self.data, self.record)
        setalpha_23(self.data, self.record)
        setalpha_53(self.data, self.record)
        setalpha_54(self.data, self.record)
        setalpha_101(self.data, self.record)
