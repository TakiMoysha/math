import math
import random
import numpy as np
from math import exp
import seaborn as sns
import matplotlib.pylab as plt


# def getGaussVariable(mean, deviation, n=6):
#     V = 0
#     for i in range(n):
#         V += random.random()
#     meanV = V-(n/2)
#     deviationV = math.sqrt(12/n)
#     X = (deviation*(deviationV*meanV))+mean
#     return X



# def getXArray(mean, deviation, N):
# 	array = []
# 	for i in range(N):
# 		array.append(getGaussVariable(mean, deviation))
# 	return array


# def additions(data, s, k):# Определение границ и интервалов группировки
#     alpha = (1+s)*min(data) # Минимальное значение из выборки Гаусса
#     betta = (1+s)*max(data) # Максимальное значение из выборки Гаусса
#     delta = (1+s)*(betta - alpha)
#     deltaX = delta/k # Длинна интервала
#     lenghtLeft = lambda i: (alpha + (i-1)*deltaX) # Границы i-го интервала
#     lenghtRight = lambda i: (alpha + i*deltaX) # Границы i-го интервала



def getXArray(mean, deviation, N):
    return np.random.normal(mean, deviation, N)


mean = 0 # среднее значение
deviation = 0.1 # среднеквадратичное отклонение
k = 10 # Кол-во интервалов
s = 0 # Поправочный множитель
N = 1500

n = 6 # Обычно n берется 6 или 12
# C = 1/(b-a)

def getD(data, M, a=0, b=0, n=6):
    sum = 0
    # Используется для проверки и отладки практических значений
    teorM = n/2  #теоретическое значение мат ожидания
    teorD = n/12 #теоретическое значение дисперсии
    for i in range(len(data)):
        sum += (data[i]-M)**2
    res = sum/len(data)
    return res, teorM, teorD


XArray = getXArray(mean, deviation, N)
M = sum(XArray)/N
D, teorM, teorD = getD(XArray, M)
print('Теоретические значения:\n\tМатематическое ожидание: %.2f\n\tДисперсия: %.2f' % (teorM, teorD))
print('Практическое значения:\n\tМатематическое ожидание: %.8f\n\tДисперсия: %.8f' % (M, D))

# Строим графики
# Гистограмма распределения гаусса
fig = plt.figure(figsize=(10,8), dpi=80)
ax_1 = fig.add_subplot(2, 1, 1)
ax_1.set(title='Распределение по гаусскому закону')
plt.grid(linestyle='--', alpha=0.5)
sns.distplot(XArray, bins=k, color="g", kde_kws={'linewidth':0.00001})
# plt.axhline(y=C)

# Построение полигона накопленных частот (frequency polygon)
ax_2 = fig.add_subplot(2, 2, 1)
columnSaturation, _, _ = ax_2.hist(XArray, bins=k)# columnSaturation - хранит кол-во точек в каждом столбце
plt.delaxes(ax_2)# delete ax_2 from the figure
arrayF_q=[] # Считаем выборочную вероятность (высоты столбцов)
for i in range(k):
    F_q = columnSaturation[i]/N
    arrayF_q.append(F_q)
print(columnSaturation, "\n", arrayF_q)
# вывод гистограммы 
ax_2 = fig.add_subplot(212)
ax_2.grid(linestyle='--', alpha=0.5)
ax_2.set(title="Frequency polygon")
# plt.bar(x, y)
plt.bar(columnSaturation, arrayF_q,  
         color = 'blue', alpha = 0.7, zorder = 2)

plt.show()