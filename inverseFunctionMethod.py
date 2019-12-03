import random
import seaborn as sns
import matplotlib.pyplot as plt


def getVarriable():
    ksi = random.random()
    f = lambda j: (b-a)*j+a
    return f(ksi)

def getArray():
    list = []
    for i in range(N):
        list.append(getVarriable())
    return list


# a = int(input("A:"))
# b = int(input("B:"))
# k = int(input("Bins:"))
# N = int(input("Выборка:"))
a, b, k = 5, 10, 9
# M = (b-a)/2
# D = ((b-a)**2)/12
C = 1/(b-a)
N = 1000
data = getArray() # f(ksi) 

def getVarriableFun(x):
    f = lambda x: (x-a)/(b-a)
    return f(x)


def getArrayFun():
    list = []
    for i in range(N):
        list.append(getVarriableFun(data[i]))
    return list


def DM(arraylist):
    summaM = 0
    for i in range(N):
        summaM += arraylist[i]
    mathO = summaM/N
    print("12:", mathO)

    summaD = 0
    for i in range(N):
        summaD = (arraylist[i]-mathO)
    mathD = summaD**2/N
    print("12123:", mathD)
    return mathO, mathD


dataFun = getArrayFun()
dm = DM(dataFun)
print('Математическое ожидание: %.8f\nДисперсия: %.8f' % (dm[0], dm[1]))


fig = plt.figure(figsize=(12, 10), dpi= 80) # Размер окна

# ax_2 = fig.add_subplot(2, 2, 2)
# ax_2.set(title='2')
# ax_2.grid(linestyle='--', alpha=0.5)
# columnSaturation, bins, _ = ax_2.hist(data, bins=k) # Для получения кол-ва точек в интервалах на гистограмме

ax_2 = fig.add_subplot(2, 2, 1)
ax_2.set(title='1')
ax_2.grid(linestyle='--', alpha=0.5)
columnSaturation, bins, _ = ax_2.hist(dataFun, bins=k)

array =[]
for i in range(8):
    F_q = columnSaturation[i]/N
    array.append(F_q)
# delete ax_2 from the figure
plt.delaxes(ax_2)

ax_1 = fig.add_subplot(1, 1, 1, sharex=ax_2)
ax_1.set(title='3')
ax_1.grid(linestyle='--', alpha=0.5)
sns.distplot(data, bins=k, color="g", kde_kws={'linewidth':0.00001})
ax_1.axhline(y=C)

plt.show()