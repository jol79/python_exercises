import seaborn as sns


titanic = sns.load_dataset('titanic')

""" check for null values """
print('Before cleaning the NaN values: {}\nWith size = {}'.format(titanic.isnull().sum(), titanic.shape))

""" replacing the NaN rows """
titanic.dropna(inplace=True)
print('After cleaning the NaN values: {}\nWith size = {}'.format(titanic.isnull().sum(), titanic.shape))

""" check the duplicated rows """
print(titanic[titanic.duplicated(keep=False)])
# drop the duplications
titanic.drop_duplicates(keep='first', inplace=True)
# confirm that deduplication success
print(titanic[titanic.duplicated(keep=False)])
