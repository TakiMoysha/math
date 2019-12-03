import math
import random
import seaborn as sns
import matplotlib.pylab as plt
from scipy.integrate import quad

# a, b = -0.25, 0.25
a, b = 0, 10
M = 6
# fun = quad(f, 0, 5)
k=9


def getNeimanVariable():
    f = lambda x: math.pi * math.cos(2*math.pi*x) # ф-ция по которой проверяется случайная величина
    # f = lambda x: 2*x # ф-ция по которой проверяется случайная величина
    r_1 = random.random()
    r_2 = random.random()
    X_0 = a+(r_1*(b-a))
    etta = r_2*M
    if etta > f(X_0):
        return(getNeimanVariable())
    else:
        return X_0


def getNeimanArray():
    array = []
    for i in range(1000):
        array.append(getNeimanVariable())
    return array


M = (b-a)/2
D = ((b-a)**2)/12
C = 1/(b-a)

def DM():
    summaM = 0
    for i in range(N):
        summaM += data[i]
    mathO = summaM/N

    summaD = 0
    for i in range(N):
        summaD = (data[i]-mathO)
    mathD = summaD/N
    return mathO, mathD

print('Математическое ожидание: %.4f\nДисперсия: %.4f' % (DM()[0], DM()[1]))

data = getNeimanArray()
# Построение графиков
# fig = plt.figure(figsize=(10,8), dpi= 80) # Размер окна
# ax_1 = fig.add_subplot(2, 1, 2)
# ax_2 = fig.add_subplot(2, 1, 1)
# ax_1.set(title='Neiman distribution')
# ax_2.set(title='Distribution density')
# ax_1.grid(linestyle='--', alpha=0.5)
# ax_2.grid(linestyle='--', alpha=0.5)
# columnSaturation, bins, _ = ax_1.hist(data, bins=k) # Кол-во элементов в каждом столбце, центры столбиков
# sns.distplot(data, bins=k, color="g", hist_kws={'alpha':.7}, kde_kws={'linewidth':3})
# print(columnSaturation)
# plt.show()

plt.grid(linestyle='--', alpha=0.5)
sns.distplot(data, bins=k, color="g", kde_kws={'linewidth':0.00001})
plt.axhline(y=C)
plt.show()