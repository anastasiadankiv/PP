import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

plt.rcParams['figure.figsize'] = (10, 5)

complaints = pd.read_csv('NYC_Jobs.csv')
print('Перші 10 запписів датасету:')
print(complaints[:10])
print()
print('Перші 10 записів у колонці Agency')
print(complaints['Agency'][:10])
 print()
# print('Усі записи у колонках Agency, Business Title, Work Location 1:')
# print(complaints[['Agency', 'Business Title', 'Work Location 1']])
# print()
# print('назви агентств та кількість вакансій, які вони подали.')
# print()
# complaint_counts = complaints['Agency'].value_counts()
# print(complaint_counts)
# complaint_counts.plot(kind='bar')
# plt.show()