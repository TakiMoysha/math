import numpy as np
import matplotlib.pylab as plt

mean = 0
deviation = 1
k = 9 # Кол-во интервалов

#np.random.seed(10)
data = np.random.normal(mean,deviation,1000)
columnSaturation = plt.hist(data, k) # Кол-во элементов в каждом столбце, центры столбиков
plt.show()