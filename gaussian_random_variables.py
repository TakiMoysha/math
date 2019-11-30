import math
import random
import numpy as np
from math import exp
from scipy.integrate import quad
import matplotlib.pylab as plt


mean = 0 # среднее значение
deviation = 1 # среднеквадратичное отклонение
k = 10 # Кол-во интервалов
s = 0 # Поправочный множитель



def getGaussArrayVariable(mean, deviation): 
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
		array.append(getGaussArrayVariable(mean, deviation))
	return array


data = getGaussArray(mean, deviation)


# Определение границ и интервалов группировки
alpha = (1+s)*min(data) # Минимальное значение из выборки Гаусса
betta = (1+s)*max(data) # Максимальное значение из выборки Гаусса
delta = (1+s)*(betta - alpha)
deltaX = delta/k # Длинна интервала
# print(deltaX)
lenghtLeft = lambda i: (alpha + (i-1)*deltaX) # Границы i-го интервала
lenghtRight = lambda i: (alpha + i*deltaX) # Границы i-го интервала

columnSaturation = plt.hist(data, bins=k) # Кол-во элементов в каждом столбце, центры столбиков
print(columnSaturation[0])
plt.show()