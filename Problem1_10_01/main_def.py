# This is the main program exacutes back-testing system
# First draft 2016/10/2
# This draft 2016/10/6


from datahandler import DataHandler
from portfolio import Portfolio
from setstrategy import SetStrategy
from analyzer import Analyzer

# Import data from module 'datahandler'
data = DataHandler('中证500测试数据.csv')

# Initialize portfolio which records each trading
record = Portfolio()

# Use sample strategy to test the system
strategy = SetStrategy(data, record, -0.5, 0.5, 1000000)

# Calculate analysis indices and plot returns
analyzer = Analyzer(data.time_, record)
