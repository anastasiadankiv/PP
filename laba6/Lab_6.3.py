import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

plt.rcParams['figure.figsize'] = (10, 5)

complaints = pd.read_csv('NYC_Jobs.csv')

print('назви агентств та кількість вакансій, які вони подали.')
print()
complaint_counts = complaints['Agency'].value_counts()
print(complaint_counts)
complaint_counts.plot(kind='bar')
plt.show()