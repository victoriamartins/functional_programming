import pandas as pd
from functools import reduce


def profit(info):
    if info[2] > info[3]:
        return True
    else:
        return False


data = pd.read_csv('data.csv')
income_column = data.iloc[:, 2].values
expenses_column = data.iloc[:, 3].values

income_is_bigger = filter(profit, data.values)

total = map(lambda inc, exp: inc-exp, income_column, expenses_column)

sum_income = reduce(lambda inc, init: inc+init, income_column, 0)
sum_expenses = reduce(lambda exp, init: exp+exp, expenses_column, 0)
mean_profit = (sum_income - sum_expenses)/5
