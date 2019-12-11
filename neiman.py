# -*- coding: utf-8 -*-

import math
from random import random
import seaborn as sns
import numpy as np
import pylab
import matplotlib.pylab as plt
from scipy.integrate import quad

def getData(a, b, N, sigma):
    data = []

    def getDataVariable(a, b, sigma):
        w = lambda x: (x/sigma**2)*math.exp((-x**2)/(2*(sigma**2))) # рассчитать при числах
        XY=[random(), random()]
        Kx_1 = (a+((b-a)*XY[0]))
        Kx_2 = XY[1]*w(1)
        if Kx_2 <= w(Kx_1):
            return(Kx_1)
        else:
            return getDataVariable(a, b, sigma)

    for i in range(N):
        data.append(getDataVariable(a, b, sigma))
    return data


def getD(data, M):
    sum = 0
    for i in range(len(data)):
        sum += (data[i]-M)**2
    res = sum/len(data)
    return res


a, b = 0, 9
k=11
sigma=1
N=1000
dataX = getData(a, b, N, sigma)

teorM = (math.sqrt(math.pi*2)/2)*sigma # теоретическое значение мат ожидания
teorD = -(sigma**2)*((2-math.pi)/2) # теоретическое значение дисперсии
M = sum(dataX)/N
D = getD(dataX, M)
print('Теоретические значения:\n\tМатематическое ожидание: %.2f\n\tДисперсия: %.2f' % (teorM, teorD))
print('Практическое значения:\n\tМатематическое ожидание: %.8f\n\tДисперсия: %.8f' % (M, D))

fig = plt.figure(figsize=(10, 6), dpi=90) # Размер окна
ax_1 = fig.add_subplot(2, 1, 1)
ax_1.set(title='Распределение method Neiman')
plt.grid(linestyle='--', alpha=0.5)

# Построение на полигоне накопленных частот ф-ции плотности распределения
xAx = np.arange(a, b, 0.01)
xAxfun = []
for i in range(len(xAx)): 
    xAxfun.append((xAx[i]/sigma**2)*math.exp(-(xAx[i]**2)/(2*(sigma**2))))
ax_1.plot(xAx, xAxfun)
pylab.xlim(a-((b-a)/10), b+((b-a)/10))
# pylab.ylim(0, 1)
sns.distplot(dataX, bins=k, color="g", kde_kws={'linewidth':0.00001})

# Построение полигона накопленных частот (frequency polygon)
ax_2 = fig.add_subplot(2, 2, 1)
columnSaturation, _, _ = ax_2.hist(dataX, bins=k) # columnSaturation - хранит кол-во точек в каждом столбце
plt.delaxes(ax_2) # delete ax_2 from the figure
arrayF_q=[] # Считаем выборочную вероятность (высоты столбцов)
for i in range(k):
    F_q = columnSaturation[i]/N
    arrayF_q.append(F_q)
# print(columnSaturation, "\n", arrayF_q)
# вывод гистограммы 
ax_2 = fig.add_subplot(212)
ax_2.grid(linestyle='--', alpha=0.5)
ax_2.set(title="Frequency polygon")
# plt.bar(x, y)


def getAxBar(data):
    array = []
    array.append(data[0])
    for i in range(1, len(data)):
        array.append((data[i]+array[i-1]))
    return array


# Построение на полигоне накопленных частот ф-ции плотности распределения
xAx = np.arange(a, b, 0.1)
xAxfun = []
for i in range(len(xAx)): 
    xAxfun.append((1-math.exp(-(xAx[i]**2)/(2*sigma**2))))
ax_2.plot(xAx, xAxfun)
pylab.xlim(a-((b-a)/10), b+((b-a)/10))
# pylab.ylim(0, 1)

xBar = getAxBar(columnSaturation)
yBar = getAxBar(arrayF_q)
plt.bar(xBar, yBar,
         color = 'blue', alpha = 0.5, zorder = 0.5)

plt.show()