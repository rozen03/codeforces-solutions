#!/usr/bin/env python3
from collections import namedtuple
from itertools import accumulate
n,m= tuple(map(int, input().split()))
lista = list(map(int, input().split()))
mood = list(map(int, input().split()))
acumulada = list(accumulate(lista))
rangos=[]
minimau =0
sumamiau=0
for k,i in enumerate(acumulada):
    if (i<0 and i<minimau):
        minimau=i
        rangos.append((lista[k],-i))
#print("acumulada=",acumulada)
print("rangos=",rangos)
rangis =[]
for indice,(val,i) in enumerate(rangos):
     if(indice==0):
        #sumamiau+=-val
        rangis.append(i)
        continue
    if(sumamiau>=i):
        continue
    sumamiau+=-val
    rangis.append(i)
print(rangis)
tam = len(rangis)
for i in mood:
    for k,j in enumerate(rangis):
        if i<=j:
            print(tam-k)
            break
    else:
        print(0)
