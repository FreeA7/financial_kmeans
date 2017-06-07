# This module sets strategies and you can change your strategies here
# First draft 2016/10/2
# This draft 2016/10/6


import numpy as np


class TestFan(object):

    def __init__(self, k_means, record, data, result, cash):

        for j in range(19):
            result.cash.append(cash)
            result.record.append(0)
            result.portfolio_volume.append(0)
            result.portfolio_value.append(0)


        for i in range(19, len(record.alpha1) + 19):
            vec = np.array((record.alpha1[i - 19], record.alpha2[i - 19], record.alpha3[
                           i - 19], record.alpha4[i - 19], record.alpha5[i - 19]))
            dist0 = np.linalg.norm(vec - k_means.k_means.cluster_centers_[0])
            dist1 = np.linalg.norm(vec - k_means.k_means.cluster_centers_[1])

# A point that is valuable to be mentioned here is algo cluster can't 
# decide which cluster is cluster 0 and which is cluster 1
# Thus, to avoid obtain inverse results I add an 'if' to keep the result right
            if not k_means.key:
                if dist0 > dist1:
                    result.record.append(-1 *
                                         int(result.portfolio_volume[-1] * 0.2))
                    result.cash.append(
                        result.cash[-1] - (result.record[-1] * data.close[i]))
                    result.portfolio_volume.append(
                        result.portfolio_volume[-1] + result.record[-1])
                    result.portfolio_value.append(
                        result.portfolio_volume[-1] * data.close[i])
                else:
                    result.record.append(
                        int((result.cash[-1] * 0.2) / data.close[i]))
                    result.cash.append(
                        result.cash[-1] - (result.record[-1] * data.close[i]))
                    result.portfolio_volume.append(
                        result.portfolio_volume[-1] + result.record[-1])
                    result.portfolio_value.append(
                        result.portfolio_volume[-1] * data.close[i])
            else:
                if dist0 < dist1:
                    result.record.append(-1 *
                                         int(result.portfolio_volume[-1] * 0.2))
                    result.cash.append(
                        result.cash[-1] - (result.record[-1] * data.close[i]))
                    result.portfolio_volume.append(
                        result.portfolio_volume[-1] + result.record[-1])
                    result.portfolio_value.append(
                        result.portfolio_volume[-1] * data.close[i])
                else:
                    result.record.append(
                        int((result.cash[-1] * 0.2) / data.close[i]))
                    result.cash.append(
                        result.cash[-1] - (result.record[-1] * data.close[i]))
                    result.portfolio_volume.append(
                        result.portfolio_volume[-1] + result.record[-1])
                    result.portfolio_value.append(
                        result.portfolio_volume[-1] * data.close[i])
