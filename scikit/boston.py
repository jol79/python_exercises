from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt


boston = datasets.load_boston()

# print(boston.feature_names)
# print(boston.target)


""" converting to df """
boston_df = pd.DataFrame(boston.data)
boston_df.columns = boston.feature_names
boston_df['target'] = boston.target


""" short analysis """
# plt.hist(boston.target)
# plt.title('Houses in Boston prices analysis'); plt.xlabel('price 1k * value ($)'); plt.ylabel('count')
# plt.show()
# CRIM vs Price
plt.scatter(boston.feature_name, boston.target)
plt.title('CRIM vs Price'); plt.xlabel('CRIM'); plt.ylabel('Price')
plt.show()


""" dividing into 2 subsets (train and test) """

