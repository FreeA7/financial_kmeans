# This module excutes the main program to cluster aplhas
# First draft 2016/10/6
# This draft 2016/10/6


from setalphas import SetAlphas
from k_mean_cluster import KmeanCluster
from datahandler2 import DataHandler2
from record import Record

# Import data from module 'datahandler2'
data = DataHandler2('stock_smaple.csv').data

# Initialize portfolio which records each alpha
record = Record()

# Set alphas
SetAlphas(data, record)

# Import cluster results from module kmeancluaster and show
k_means = KmeanCluster(record, data.returni).k_means

