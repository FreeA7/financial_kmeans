# This module records changes of the portfolio
# First draft 2016/10/2
# This draft 2016/10/6


class Portfolio(object):

    def __init__(self):

        # Part I: trading record
        self.alpha1 = []  # 判断因子
        self.open_price = []  # 分钟开盘价
        self.close_price = []  # 分钟收盘价
        self.high_price = []  # 分钟最高价
        self.low_price = []  # 分钟最低价
        self.trade_volume = []  # 分钟交易量
        self.trade_value = []  # 分钟交易额
        self.record = []  # 买卖操作量 -卖 +买 0不买不卖
        self.cash = []  # 现金
        self.portfolio_volume = []  # 仓位
        self.portfolio_value = []  # 资产价值

        # Part II: analysis indices
        self.annu_return = []
        self.annu_volatility = []
        self.max_drawdown = 0
        self.sharpe_ratio = 0
