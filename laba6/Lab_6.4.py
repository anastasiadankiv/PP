import pandas as panda
import matplotlib.pyplot as plt
import numpy

contain=panda.read_csv('NYC_Jobs.csv')
catagory=contain[['Job Category','Salary Range From']].copy()
group=catagory.groupby('Job Category').aggregate(numpy.median)
print(group)
group.plot(kind='bar')
plt.show()
location=contain[['Work Location','Salary Range From']].copy()
group2=location.groupby('Work Location').aggregate(numpy.median)
print(group)
group2.plot(kind='bar')
plt.show()