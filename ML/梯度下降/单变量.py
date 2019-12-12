'''
1, 2, 3, 4, 5, 6, 7
150, 200, 250, 300, 350, 400, 600
6450, 7450, 8450, 9450, 11450, 15450, 18450
'''

import math
import numpy as np
from matplotlib import pyplot

# Size of the points dataset.
m = 7

area = [150, 200, 250, 300, 350, 400, 600]
price = [6450, 7450, 8450, 9450, 11450, 15450, 18450]


# The Learning Rate alpha.
alpha = 0.00000001
theta1 = 1
theta2 = 1

temp = 0
k = 0
pyplot.scatter(area,price)
while math.fabs(theta1-temp)>1e-5 and math.fabs(theta2 - temp)>1e-5:
    sum = 0
    k += 1
    for i in range(0,7):
        sum += theta1 + theta2 * area[i] - price[i]
    sum /= m
    temp = theta1
    theta1 = theta1 - sum * alpha

    sum = 0
    for i in range(0,7):
        sum += (theta1 + theta2 * area[i] - price[i]) * area[i]
    sum /= m
    theta2 = theta2 - sum * alpha
    if(k%100==0):
        x = np.arange(100, 700, 100)
        y = theta2 * x + theta1
        pyplot.plot(x, y)


print(k, theta1, theta2)


pyplot.xlabel('area')
pyplot.ylabel('price')
pyplot.show()