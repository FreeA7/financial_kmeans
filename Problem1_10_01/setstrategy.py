# This module sets strategies and you can change your strategies here
# First draft 2016/10/2
# This draft 2016/10/6


def alpha1(data, record, low, up, cash):

    # Initial settings for 1st minute
    record.open_price.append(data.open_price[0])
    record.close_price.append(data.close_price[0])
    record.record.append(0)
    record.cash.append(cash)
    record.portfolio_volume.append(0)
    record.portfolio_value.append(0)

    for i in range(1, len(data.data)):
        record.alpha1.append((data.close_price[i - 1] - data.open_price[i - 1]) / (
            (data.high_price[i - 1] - data.low_price[i - 1]) + 0.001))

        record.open_price.append(data.open_price[i])
        record.close_price.append(data.close_price[i])

# The strategy used here is simple rather than reasonable:
# If alpha < -0.5, buy using 20% of the money in the cash account;
# If alpha > 0.5, sell 20% of the asset in portfolio;
# If -0.5<= alpha <= 0.5, do nothing but 思考人生

        if record.alpha1[i - 1] < low:
            record.record.append(
                int((record.cash[i - 1] * 0.2) / data.open_price[i]))
            record.cash.append(
                record.cash[i - 1] - (record.record[i] * data.open_price[i]))
            record.portfolio_volume.append(record.portfolio_volume[
                                           i - 1] + record.record[i])
            record.portfolio_value.append(record.portfolio_volume[
                                          i] * data.close_price[i])

        elif record.alpha1[i - 1] > up:
            record.record.append(-1 *
                                 int(record.portfolio_volume[i - 1] * 0.2))
            record.cash.append(
                record.cash[i - 1] - (record.record[i] * data.open_price[i]))
            record.portfolio_volume.append(record.portfolio_volume[
                                           i - 1] + record.record[i])
            record.portfolio_value.append(record.portfolio_volume[
                                          i] * data.close_price[i])

        else:
            record.record.append(0)
            record.cash.append(record.cash[i - 1])
            record.portfolio_volume.append(record.portfolio_volume[i - 1])
            record.portfolio_value.append(record.portfolio_volume[
                                          i] * data.close_price[i])
            record.alpha1.append(0)


class SetStrategy(object):

    def __init__(self, data, record, low, up, cash, typee='alpha1'):
        self.data = data
        self.record = record
        self.low = low
        self.up = up
        self.cash = cash
        self.typee = typee

        alpha1(self.data, self.record, self.low, self.up, self.cash)
