import math
import random
import numpy as np
from math import exp
import seaborn as sns
import matplotlib.pylab as plt


def getGaussVariable(mean, deviation): 
    n = 6 # Обычно n  берется 6 или 12
    V = 0
    for i in range(n):
        V += random.random()
    meanV = V-(n/2)
    deviationV = math.sqrt(12/n)
    X = (deviation  * (deviationV * meanV)) + mean
    return X


def getGaussArray(mean, deviation):
	array = []
	for i in range(1000):
		array.append(getGaussVariable(mean, deviation))
	return array


def additions(data, s, k):# Определение границ и интервалов группировки
    alpha = (1+s)*min(data) # Минимальное значение из выборки Гаусса
    betta = (1+s)*max(data) # Максимальное значение из выборки Гаусса
    delta = (1+s)*(betta - alpha)
    deltaX = delta/k # Длинна интервала
    lenghtLeft = lambda i: (alpha + (i-1)*deltaX) # Границы i-го интервала
    lenghtRight = lambda i: (alpha + i*deltaX) # Границы i-го интервала


mean = 0 # среднее значение
deviation = 1 # среднеквадратичное отклонение
k = 10 # Кол-во интервалов
s = 0 # Поправочный множитель

data = getGaussArray(mean, deviation)
# Построение графиков
fig = plt.figure(figsize=(10,10), dpi= 80) # Размер окна 
ax_1 = fig.add_subplot(2, 1, 2)
ax_2 = fig.add_subplot(2, 1, 1)
ax_1.set(title='Gaussian distribution')
ax_2.set(title='Distribution density')
ax_1.grid(linestyle='--', alpha=0.5)
ax_2.grid(linestyle='--', alpha=0.5)
columnSaturation, bins, _ = ax_1.hist(data, bins=k) # Кол-во элементов в каждом столбце, центры столбиков
sns.distplot(data, bins=k, color="g", hist_kws={'alpha':.7}, kde_kws={'linewidth':3})
print(columnSaturation)

plt.show()
