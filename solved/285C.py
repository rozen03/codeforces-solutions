#!/usr/bin/env python3
n= map(int, input().split())
lista = list(map(int, input().split()))
lista= sorted(lista)
res=0
for k,num in enumerate(lista):
    res+=abs(k+1-num)
print(res)
