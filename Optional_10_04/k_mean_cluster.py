# This module implements k-mean cluster algo to category alphas
# Fist draft 2016/10/3
# This draft 2016/10/6


from sklearn import preprocessing
from sklearn.cluster import KMeans
import numpy as np


class KmeanCluster(object):

    def __init__(self, record, returni):

        record.alpha1 = preprocessing.scale(record.alpha1)
        record.alpha2 = preprocessing.scale(record.alpha2)
        record.alpha3 = preprocessing.scale(record.alpha3)
        record.alpha4 = preprocessing.scale(record.alpha4)
        record.alpha5 = preprocessing.scale(record.alpha5)

        merged_data = np.vstack(
            (record.alpha1, record.alpha2, record.alpha3, record.alpha4, record.alpha5))
        merged_data_transposed = np.transpose(merged_data)
        k_means = KMeans(n_clusters=2, max_iter=5000).fit(
            merged_data_transposed)

# Obtain the return rates in each cluster

        cluster_0_return_rate = []
        cluster_1_return_rate = []

        for i in range(18, len(k_means.labels_) + 18):
            if k_means.labels_[i - 18] == 1:
                cluster_1_return_rate.append(returni[i])
            else:
                cluster_0_return_rate.append(returni[i])

        mean_return_rate = np.mean(returni[18:])
        mean_cluster_0_return_rate = np.mean(cluster_0_return_rate)
        mean_cluster_1_return_rate = np.mean(cluster_1_return_rate)
        if mean_cluster_0_return_rate < mean_cluster_1_return_rate:
            self.key = 1
        else:
            self.key = 0

        std_return_rate = np.std(returni[18:])
        std_cluster_0_return_rate = np.std(cluster_0_return_rate)
        std_cluster_1_return_rate = np.std(cluster_1_return_rate)

        print('***** Cluster Finished *****')
        print('Average daily return and volatility (overall)：' +
              str(mean_return_rate) + '\t' + str(std_return_rate))
        print('Average daily return and volatility (cluster 0)：' + str(mean_cluster_0_return_rate) +
              '\t' + str(std_cluster_0_return_rate))
        print('Average daily return and volatility (cluster 1)：' + str(mean_cluster_1_return_rate) +
              '\t' + str(std_cluster_1_return_rate) + '\n')

        self.k_means = k_means
