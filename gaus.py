import math
import random
import numpy as np
from math import exp
import seaborn as sns
import matplotlib.pylab as plt


def getXArray(mean, deviation, N):
    return np.random.normal(mean, deviation, N)


mean = 0 # среднее значение
deviation = 0.5 # среднеквадратичное отклонение sigma
k = 11 # Кол-во интервалов
s = 0 # Поправочный множитель
N = 2000

n = 6 # Обычно n берется 6 или 12

def getD(data, M, a=0, b=0, n=6):
    sum = 0
    # Используется для проверки и отладки практических значений
    teorM = n/2  #теоретическое значение мат ожидания
    teorD = math.sqrt(n/12) #теоретическое значение дисперсии
    for i in range(len(data)):
        sum += (data[i]-M)**2
    res = sum/len(data)
    return res, teorM, teorD


XArray = getXArray(mean, deviation, N)
M = sum(XArray)/N
D, teorM, teorD = getD(XArray, M)
# print('Теоретические значения:\n\tМатематическое ожидание: %.2f\n\tДисперсия: %.2f' % (teorM, teorD))
# print('Практическое значения:\n\tМатематическое ожидание: %.8f\n\tДисперсия: %.8f' % (M, D))

# Строим графики
# Гистограмма распределения гаусса
fig = plt.figure(figsize=(10,8), dpi=80)
ax_1 = fig.add_subplot(2, 1, 1)
ax_1.set(title='Распределение по гаусскому закону')
plt.grid(linestyle='--', alpha=0.5)

# Построение на полигоне накопленных частот ф-ции плотности распределения
xAx = np.arange(-3, 3, 0.1) # Изменив 3 аргумент изменяется гладкость ф-ции распределения
xAxfun = []
for i in range(len(xAx)):
    xAxfun.append((math.exp(-(xAx[i]**2)/(2*deviation**2)))*(1/(deviation*math.sqrt(math.pi*2))))
ax_1.plot(xAx, xAxfun)
sns.distplot(XArray, bins=k, color="g", kde_kws={'linewidth':0.00001})

# Построение полигона накопленных частот (frequency polygon)
ax_2 = fig.add_subplot(2, 2, 1)
columnSaturation, _, _ = ax_2.hist(XArray, bins=k)# columnSaturation - хранит кол-во точек в каждом столбце
plt.delaxes(ax_2)# Удаляет ax_2 из fig
arrayF_q=[] # Считаем выборочную вероятность (высоты столбцов)
for i in range(k):
    F_q = columnSaturation[i]/N
    arrayF_q.append(F_q)

# вывод гистограммы
ax_2 = fig.add_subplot(212)
ax_2.grid(linestyle='--', alpha=0.5)
ax_2.set(title="Frequency polygon")


def getAxBar(data):
    array = []
    array.append(data[0])
    for i in range(1, len(data)):
        array.append(data[i]+array[i-1])
    return array

# Построение на полигоне накопленных частот ф-ции Плотность вероятности
xAx = np.arange(0, N, 0.1)
yAx = []
for i in range(len(xAx)):
    yAx.append(1*(1+math.erf((xAx[i]-mean)**2/(4000*N*deviation**2)))-1)

ax_2.plot(xAx, yAx)

xBar = getAxBar(columnSaturation)
yBar = getAxBar(arrayF_q)

plt.bar(xBar, yBar,
         color = 'blue', alpha = 0.7, zorder = 2, width=3)

plt.show()
