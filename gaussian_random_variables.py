import math
import random
import numpy as np


def getArrayVariable():
    mean = 0 # среднее значение
    deviation = 1 # среднеквадратичное отклонение
    n = 6 # Обычно n  берется 6 или 12
    V = 0
    N = 10 # кол-во точек
    for i in range(N):
        result = list()
        for i in range(n):
            V += random.random()
        meanV = V-(n/2)
        deviationV = math.sqrt(12/n)
        X = (deviation  * (deviationV * meanV)) + mean
        result.append(X)
    return result


print(getArrayVariable())