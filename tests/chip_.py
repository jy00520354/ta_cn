import numpy as np

from ta_cn.chip import chip, WINNER, COST

high = np.array([10.4, 10.2, 10.2, 10.4, 10.5, 10.7, 10.7, 10.7, 10.8, 10.9])
low = np.array([10.3, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9])
avg = np.array([10.3, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9])
close = np.array([10.3, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9])
turnover = np.array([0.3, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

step = 0.1
out, columns = chip(high, low, avg, turnover, step=step)
print(out.sum(axis=1))
print(columns)
x = WINNER(out, columns, close)
print(x)
y = COST(out, columns, 0.85)
print(y)
