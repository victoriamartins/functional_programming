import pandas as pd
data = pd.read_csv('data.csv')

total = data['income'] - data['expenses']

income_is_bigger = list()
for i in range(0, 5):
    if data['income'][i] > data['expenses'][i]:
        income_is_bigger.append(data.iloc[i, :])

sum_expenses = 0
sum_income = 0
for i in range(0, 5):
    sum_income += data['income'][i]
    sum_expenses += data['expenses'][i]
mean_profit = (sum_income - sum_expenses)/5
