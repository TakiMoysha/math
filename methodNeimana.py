import math
import random
import seaborn as sns
import matplotlib.pylab as plt
from scipy.integrate import quad

# a, b = -0.25, 0.25
a, b = 0, 100
M = 6
# fun = quad(f, 0, 5)
k=2


def getNeimanVariable():
    # f = lambda x: math.pi * math.cos(2*math.pi*x) # ф-ция по которой проверяется случайная величина
    f = lambda x: 2*x # ф-ция по которой проверяется случайная величина
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



data = getNeimanArray()
# Построение графиков
fig = plt.figure(figsize=(10,10), dpi= 80) # Размер окна 
ax_1 = fig.add_subplot(2, 1, 2)
ax_2 = fig.add_subplot(2, 1, 1)
ax_1.set(title='1111')
ax_2.set(title='2222')
ax_1.grid(linestyle='--', alpha=0.5)
ax_2.grid(linestyle='--', alpha=0.5)
columnSaturation, bins, _ = ax_1.hist(data, bins=k) # Кол-во элементов в каждом столбце, центры столбиков
sns.distplot(data, bins=k, color="g", hist_kws={'alpha':.7}, kde_kws={'linewidth':3})
print(columnSaturation)
plt.show()