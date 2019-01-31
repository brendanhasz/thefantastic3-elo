
# Packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
nrows = 10000 #only load the first few rows
train = pd.read_csv('../input/train.csv', nrows=nrows)
test = pd.read_csv('../input/test.csv', nrows=nrows)
merchants = pd.read_csv('../input/merchants.csv', nrows=nrows)
hist_trans = pd.read_csv('../input/historical_transactions.csv', nrows=nrows)
new_merch = pd.read_csv('../input/new_merchant_transactions.csv', nrows=nrows)

# Show a histogram of the loyalty score
plt.hist(train['target'], bins=20)
plt.title('Loyalty score distribution')
plt.xlabel('Loyalty Score')
plt.ylabel('Number of entries')
plt.show()