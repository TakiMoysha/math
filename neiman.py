import math
from random import random
import seaborn as sns
import numpy as np
import matplotlib.pylab as plt
from scipy.integrate import quad


def getData(a, b, N, sigma):
    data =[]
    for i in range(N):
        w = lambda x: 1-math.exp((-x**2)/(2*(sigma**2)))
        XY=[random(), random()]
        Kx_1 = a+(b-a)*XY[0]
        Kx_2 = w(XY[1])*w(5)
        if Kx_2 <= w(Kx_1):
            data.append(Kx_1)
        else:
            i -= 1
    return data


def getD(data, M, a=0, b=0):
    sum = 0
    # Используется для проверки и отладки практических значений
    teorM = (b+a)/2  #теоретическое значение мат ожидания
    teorD = (b-a)**2/12 #теоретическое значение дисперсии
    for i in range(len(data)):
        sum += (data[i]-M)**2
    res = sum/len(data)
    return res, teorM, teorD


a, b = 0, 3
k=9
sigma=0.5
N=1000

dataX = getData(a, b, N, sigma)
M = sum(dataX)/N # Математическое ожидание
D, teorM, teorD = getD(dataX, M, a, b)
print('Теоретические значения:\n\tМатематическое ожидание: %.2f\n\tДисперсия: %.2f' % (teorM, teorD))
print('Практическое значения:\n\tМатематическое ожидание: %.8f\n\tДисперсия: %.8f' % (M, D))

fig = plt.figure(figsize=(10, 8), dpi= 80) # Размер окна
ax_1 = fig.add_subplot(2, 1, 1)
ax_1.set(title='Распределение method Nriman')
plt.grid(linestyle='--', alpha=0.5)
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
plt.bar(columnSaturation, arrayF_q, 
         color = 'blue', alpha = 0.7, zorder = 2)

plt.show()