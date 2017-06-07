# This module analyzes technical indices and plots curves
# First draft 2016/10/2
# This draft 2016/10/6

# Most of this module is the same as the one in Prolem,
# so I only note the different part.

import numpy as np
import matplotlib.pyplot as plt


class Analyzer(object):

    def __init__(self, time_, record, data):
        self.time_ = time_
        self.record = record
        self.max_value = []

# Because of the frequency of stock data is daily, I choose to calculate
# annual return, volatility, max drawdown and sharpte ratio,
# so I need the interval to help.
        interval = int((self.time_[-1] - self.time_[0]).days)

        self.interest = 0.05

        list_date = []
        list_num = []
        count = 0
        flag = 1
        j = 0

        for i in range(len(self.time_) - 1):
            if flag == 1:
                list_date.append([])
                list_num.append([])
                j += 1
                k = self.time_[i].day
                flag = 0
            list_date[j - 1].append(self.time_[i])
            list_num[j - 1].append(count)
            count += 1
            if self.time_[i + 1].day != k:
                flag = 1

        list_date.append([])
        list_num.append([])
        list_date[j].append(self.time_[-1])
        list_num[j].append(count)
        count += 1
        list_min = []
        list_value_max = []

        for i in range(len(self.record.cash) - 19):
            list_min.append(((self.record.portfolio_value[i + 19] + self.record.cash[i + 19]) - (self.record.portfolio_value[
                            i + 18] + self.record.cash[i + 18])) / (self.record.portfolio_value[i + 18] + self.record.cash[i + 18]))

        self.record.annu_volatility = np.std(list_min) * 252 / interval

        self.record.annu_return = sum(list_min) * 252 / interval

        for k in range(1, len(self.record.cash) - 19):
            max_ = self.record.portfolio_value[19] + self.record.cash[19]
            for j in range(k):
                if (self.record.portfolio_value[j + 19] + self.record.cash[j + 19]) > max_:
                    max_ = self.record.portfolio_value[
                        j + 19] + self.record.cash[j + 19]
            list_value_max.append(
                1 - ((self.record.portfolio_value[k + 19] + self.record.cash[k + 19]) / max_))
        self.record.max_drawdown = max(list_value_max)

        self.record.sharpe_ratio = (
            (self.record.annu_return - self.interest) / self.record.annu_volatility)

        print('Below is four analysis indices')
        print('Daily annual return is: ' + str(self.record.annu_return))
        print('Daily annual volatility is : ' +
              str(self.record.annu_volatility))
        print('Daily max_drawdown is: ' + str(self.record.max_drawdown))
        print('Daily sharpe ratio is: ' + str(self.record.sharpe_ratio))

        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.plot(self.time_[19:], (np.array(
            record.portfolio_value) + np.array(record.cash))[19:])
        ax1.set_ylabel('Total value of the portfolio')
        ax1.set_title('Return comparison')
        ax1.set_ylim(min(np.array(record.portfolio_value) + np.array(record.cash)) *
                     0.99, max(np.array(record.portfolio_value) + np.array(record.cash)) * 1.01)

        ax2 = ax1.twinx()
        ax2.plot(self.time_[19:], data.close[19:], 'r')
        ax2.set_ylim(min(np.array(data.close)) * 0.99,
                     max(np.array(data.close)) * 1.01)
        ax2.set_ylabel('Stock close price')

        plt.show()

