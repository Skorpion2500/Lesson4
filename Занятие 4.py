import random

############## Сортировка методом пузырька
l=list(input('Введите список:'))
for i in range(0,len(l)-1):
    for j in range(len(l)-1):
        if (l[j]>l[j+1]):
            c=l[j]
            l[j]=l[j+1]
            l[j+1]=c
print(l)
############## Создание словаря с кортежем
rgb={'red':(255,0,0),'green':(0,255,0),'blue':(0,0,255)}
print(rgb)
############## 2 случайных набора чисел
N=5
a=[]
b=[]
for i in range(N):
    a.append(random.randint(0,100))
    b.append(random.randint(0,100))
a=set(a)
b=set(b)
print(b.intersection(a))            # Входят одновременно в оба
print(a.difference(b))              # Входят только в первое, но не входят во второе
print(b.difference(a))              # Входят только во второе, но не входят в первое
print(a.symmetric_difference(b))    # Входят в первое или во второе, но не в оба из них одновременно