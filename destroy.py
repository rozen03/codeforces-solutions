#!/usr/bin/env python3
from heapq import *
from itertools import accumulate
from collections import namedtuple
from bisect import *
Rango = namedtuple("Rango", ['desde', 'hasta'], verbose=False, rename=False)


def rebuscar(rangos, indice):
    midl = len(rangos) // 2
    ranguito = rangos[midl]
    if (ranguito.desde <= indice <= ranguito.hasta):
        return ranguito
    else:
        if (indice < ranguito.desde):
            return rebuscar(rangos[:midl], indice)
        else:
            return rebuscar(rangos[midl:], indice)

n = int(input())
vectur = [0] + [int(i) for i in input().split()] + [0]  # valores de cada #O(n)
casos = [int(i) for i in input().split()]  # O(n)
sumas = list(accumulate(vectur))  # O(n)
#sumas = sumas
heap = []  # O(1)
initialRange = Rango(desde=1, hasta=n)  # O(1)
heappush(heap, ((-1) * sumas[-1], initialRange))  # O(1)
tuplasMuertas = []  # O(1)
rangos = [initialRange]  # O(1)
for i in casos:
    ranguito = rebuscar(rangos, i)  # O(log(n))
    print(ranguito)
    rangos.remove(ranguito)  # O(n)?
    insort(tuplasMuertas, ranguito)  # O(log n)?
    if(i > ranguito.desde):  # O(1)
        suma = sumas[i] - sumas[ranguito.desde]  # O(1)
        heappush(heap, ((-1) * suma, Rango(ranguito.desde, i)))  # O(log(n))
        insort(rangos, Rango(ranguito.desde, i))  # O(n)
    if(i < ranguito.hasta):
        suma = sumas[ranguito.hasta] - sumas[i]
        heappush(heap, ((-1) * suma, Rango(i, ranguito.hasta)))
        insort(rangos, Rango(i, ranguito.hasta))
    val, rangow = heap[0]
    while(rangow in tuplasMuertas):
        tuplasMuertas.remove(rangow)
        heappop(heap)
        val, rangow = heap[0]
    print((-1) * val)
