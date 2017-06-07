# This module records changes of the portfolio
# First draft 2016/10/2
# This draft 2016/10/6


class Portfolio(object):

    def __init__(self):

        # Part I: trading record
        self.record = []  # 买卖操作量 -卖 +买 0不买不卖
        self.cash = []  # 现金
        self.portfolio_volume = []  # 仓位
        self.portfolio_value = []  # 资产价值

        # Part II: analysis indices
        self.annu_return = 0
        self.annu_volatility = 0
        self.max_drawdown = 0
        self.sharpe_ratio = 0
