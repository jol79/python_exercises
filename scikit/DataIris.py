from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import numpy as np


iris = datasets.load_iris()

# print('Features of the plants: ', iris.feature_names)
# print('Plants names: ', iris.target_names)
# print('Targets: ', iris.target)


"""converting to df"""
iris_df = pd.DataFrame(iris.data)
iris_df.columns = iris.feature_names
iris_df['target'] = iris.target


""" study hours / grades """
hours = [55.1, 70.8, 29.1, 51.1, 89.3, 89.6, 12.6, 20.7, 5.1, 44.1, 3.0, 45.7, 64.9, 27.8, 67.6]
grades = [8.3, 14.8, 6.8, 11.6, 18.6, 16.0, 4.8, 3.4, 2.3, 9.3, 4.5, 11.4, 11.6, 4.4, 11.4]

# print("Hours list: {}\nGrades list: {}".format(hours, grades))

# converting lists to 2nd dimension array
hours = np.array(hours).reshape(-1, 1)
grades = np.array(grades).reshape(-1, 1)

""" visualization with matplotlib """
# plt.plot(hours, grades, 'ob')
# plt.xlabel('study hours(h)'); plt.ylabel('grades')
# plt.show()


""" dividing dataset into 2 subsets (train and test purposes) """
# use 30% for test and 70% for train
hours_train, hours_test, grades_train, grades_test = train_test_split(hours, grades, test_size=0.33)
# plt.plot(hours_train, grades_train, 'ob', label='train')
plt.plot(hours_test, grades_test, 'or', label='test')
plt.xlabel('study hours(h)'); plt.ylabel('grades')
plt.legend()
# plt.show()


""" instantiating linear regression model """
model = LinearRegression()
model.fit(X=hours_train, y=grades_train)
# using the data that I left for testing (predicting the grade based on hours spend studying)
grades_estimated = model.predict(hours_test)
# calculating model performance
R2 = model.score(hours_test, grades_test)
print('*Hours:\n{}\n*Grades test:\n{}\n*Grades estimated:\n{}\nModel performance = {}%'.format(hours_test, grades_test, grades_estimated, round(R2*100)))

# visualizing the test and train models
plt.plot(hours_train, grades_train, 'ob', label='train data')
plt.plot(hours_test, grades_estimated, label='regression line')
plt.plot(hours_test, grades_estimated, 'g*', label='grades estimated')
plt.legend(); plt.show()
