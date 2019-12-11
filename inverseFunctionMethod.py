# -*- coding: utf-8 -*-

import random
import seaborn as sns
import numpy as np
import pylab
import matplotlib.pyplot as plt

def selectionArray(N):
    list = []
    for i in range(N):
        list.append(random.random())
    return list


a, b, N, k = 0, 9, 1000, 9
# a = int(input("A:"))
# b = int(input("B:"))
# k = int(input("Bins:"))
# N = int(input("Выборка:"))
sel = selectionArray(N) # Это список рандомных кси

def getXArray(selection, a, b):
    res = []
    for i in range(N):
        fun = lambda ksi: (b-a)*ksi+a
        res.append(fun(selection[i]))
    return res


def getD(data, M, a=0, b=0):
    sum = 0
    # Используется для проверки и отладки практических значений
    teorM = (b+a)/2  #теоретическое значение мат ожидания
    teorD = (b-a)**2/12 #теоретическое значение дисперсии
    for i in range(len(data)):
        sum += (data[i]-M)**2
    res = sum/len(data)
    return res, teorM, teorD


XArray = getXArray(sel, a, b) # Это список Х_i сформированный  по рандомным кси
C = 1/(b-a)
M = sum(XArray)/N # Математическое ожидание
D, teorM, teorD = getD(XArray, M, a, b)
print('Теоретические значения:\n\tМатематическое ожидание: %.2f\n\tДисперсия: %.2f' % (teorM, teorD))
print('Практическое значения:\n\tМатематическое ожидание: %.8f\n\tДисперсия: %.8f' % (M, D))

# Построение гистограммы
fig = plt.figure(figsize=(10, 8), dpi= 80) # Размер окна
ax_1 = fig.add_subplot(2, 1, 1)
ax_1.set(title='Распределение по Обратной ф-ции')
ax_1.grid(linestyle='--', alpha=0.5)

# Построение гистограммы
sns.distplot(XArray, bins=k, color="g", kde_kws={'linewidth':0.00001})
ax_1.hlines(y=C, xmin=a, xmax=b, color='b')

# Построение полигона накопленных частот (frequency polygon)
ax_2 = fig.add_subplot(2, 2, 1)
columnSaturation, _, _ = ax_2.hist(XArray, bins=k)# columnSaturation - хранит кол-во точек в каждом столбце
plt.delaxes(ax_2)# delete ax_2 from the figure
arrayF_q=[] # Считаем выборочную вероятность (высоты столбцов)
for i in range(k):
    F_q = columnSaturation[i]/N
    arrayF_q.append(F_q)
# вывод гистограммы 
ax_2 = fig.add_subplot(212)
ax_2.grid(linestyle='--', alpha=0.5)
ax_2.set(title="Frequency polygon")


def getAxBar(data, i=0):
    array = []
    if i == 0:
        array.append(data[0])
        for i in range(1, len(data)):
            array.append(data[i]+array[i-1])
    else:
        array.append(data[0]*100)
        for i in range(1, len(data)):
            array.append((data[i]+array[i-1])*100)
    return array

# Построение на полигоне накопленных частот ф-ции плотности распределения
xAx = np.arange(0, 1000, 1)
yAx = []
for i in range(len(xAx)): 
    yAx.append((xAx[i]-a)/(b-a)/100)
ax_2.plot(xAx, yAx)
# pylab.xlim(a-((b-a)/10), b+((b-a)/10))
# pylab.ylim(0, 0.5)

xBar = getAxBar(columnSaturation)
yBar = getAxBar(arrayF_q)
plt.bar(xBar, yBar,
         color = 'blue', alpha = 0.7, zorder = 2)

plt.show()