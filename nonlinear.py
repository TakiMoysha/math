import math


# этап 1, Определение отрезков
def getSegments(a, b, n, fun):
    dx = (b - a) / n
    x1 = a
    segments = []
    while x1 <= (b - a):
        x2 = x1 + dx
        if fun(x1) * fun(x2) < 0:
            segments.append([x1, x2])
        x1 = x2
    return segments


# этап 2, Уточнение корня
def getRoots(listSegments, fun, eps):
    xl = listSegments[0]
    iter = 0
    x = xl
    y = fun(xl)
    c = abs(x-y)
    while (c<eps)^(iter<20000):
        x = y
        y = fun(x)
        c = abs(x-y)
        iter+=1
    return x



# Определение данных
a, b, n, eps = -5, 5, 9, 0.0001
# fun = lambda x: math.e ** x - 10*x
fun = lambda x: x*3 + math.cos(x) + 1


# этап 1, Определение отрезков
segments = getSegments(a, b, n, fun)
print(segments)

# этап 2, Уточнение корня
if len(segments) >= 1:
    print("Корней больше 1")
    roots = getRoots(segments[0], fun, eps)
    print(roots)
else:
    print("Нет корней")