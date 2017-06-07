# This module analyzes technical indices and plots curves
# First draft 2016/10/2
# This draft 2016/10/6


import numpy as np
from matplotlib import pyplot as plt


class Analyzer(object):

    def __init__(self, time_, record):
        self.time_ = time_
        self.record = record
        self.max_value = []
        self.interest = 0.05

# Calculate interval used to
#         interval = int((self.time_[-1] - self.time_[0]).days)

# Preprocess data for calculation of the four indices
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
        list_date[j - 1].append(self.time_[-1])
        list_num[j - 1].append(count)
        count += 1
        list_min = []
        list_value = []
        list_value_max = []

        list_value.append(self.record.cash[0] + self.record.portfolio_value[0])
        for i in range(1, len(list_date[0])):
            if (self.record.cash[list_num[0][i]] + self.record.portfolio_value[list_num[0][i]]) > list_value[0]:
                list_value[0] = self.record.cash[list_num[0][i]] + \
                    self.record.portfolio_value[list_num[0][i]]
            list_min.append((((self.record.cash[list_num[0][i]] + self.record.portfolio_value[list_num[0][i]]) - (self.record.cash[list_num[0][
                            i - 1]] + self.record.portfolio_value[list_num[0][i - 1]])) / (self.record.cash[list_num[0][i - 1]] + self.record.portfolio_value[list_num[0][i - 1]])))

# I think for data with frequency of minute,
# overall return in the whole backtest period isn't accurate enough,
# which I don't think is '清真'.
# Therefore, I calculate annual return based on every day's return below,
# which I define as 'daily annual return', 'daily annual volatility',
# 'daily max drawdown', and 'daily sharpe ratio', likewise.
        self.record.annu_volatility.append(np.std(list_min) * 252)
        list_min = []

        for i in range(1, len(list_date)):
            self.record.annu_return.append((((self.record.cash[list_num[i][-1]] + self.record.portfolio_value[list_num[i][-1]]) - (self.record.cash[list_num[
                                           i - 1][-1]] + self.record.portfolio_value[list_num[i - 1][-1]])) / (self.record.cash[list_num[i - 1][-1]] + self.record.portfolio_value[list_num[i - 1][-1]])) * 252)
            list_value.append(self.record.cash[list_num[i][
                              0]] + self.record.portfolio_value[list_num[i][0]])
            for j in range(1, len(list_date[i])):
                if (self.record.cash[list_num[i][j]] + self.record.portfolio_value[list_num[i][j]]) > list_value[i]:
                    list_value[i] = self.record.cash[list_num[i][j]] + \
                        self.record.portfolio_value[list_num[i][j]]
                list_min.append((((self.record.cash[list_num[i][j]] + self.record.portfolio_value[list_num[i][j]]) - (self.record.cash[list_num[i][
                                j - 1]] + self.record.portfolio_value[list_num[i][j - 1]])) / (self.record.cash[list_num[i][j - 1]] + self.record.portfolio_value[list_num[i][j - 1]])))
# Calculate daily annual volatility
            self.record.annu_volatility.append(np.std(list_min) * 252)
            list_min = []

        for i in range(1, len(list_date)):
            max_ = list_value[0]
            for j in range(i):
                if list_value[j] > max_:
                    max_ = list_value[j]
            list_value_max.append(
                1 - ((self.record.cash[i] + self.record.portfolio_value[i]) / max_))
# Calculate daily max_drawdown
        self.record.max_drawdown = list_value_max
# Calculate daily sharp ratio
        self.record.sharpe_ratio = ((np.array(
            self.record.annu_return) - self.interest) / np.array(self.record.annu_volatility[1:]))

        print('Below is four analysis indices')
        print('For the sake of your computer, the first ten data are shown')
        print('Daily annual return is: ' + str(self.record.annu_return[1:10]))
        print('Daily annual volatility is : ' +
              str(self.record.annu_volatility[1:10]))
        print('Daily max_drawdown is: ' + str(self.record.max_drawdown[1:10]))
        print('Daily sharpe ratio is: ' + str(self.record.sharpe_ratio[1:10]))

# Plot the total portfolio value
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
# Time is in YYYY-MM format
        ax1.plot(self.time_, (np.array(
            record.portfolio_value) + np.array(record.cash)))
        ax1.set_ylabel('Total value of the portfolio')
        ax1.set_title('Return comparison')
# Total potfolio value is on the left y-axis
        ax1.set_ylim(min(np.array(record.portfolio_value) + np.array(record.cash)) *
                     0.99, max(np.array(record.portfolio_value) + np.array(record.cash)) * 1.01)

# Plot the close price of ZZ500 index
        ax2 = ax1.twinx()
        ax2.plot(self.time_[1:], record.close_price[1:], 'r')
        ax2.set_ylim(min(np.array(record.close_price[1:])) * 0.99,
                     max(np.array(record.close_price[1:])) * 1.01)
        ax2.set_ylabel('Index close price')
# Plot two lines in one graph
        plt.show()
