#!/usr/bin/env python3

(n,k) = input().split()
n=int(n)
k=int(k)
array = []
for i in range(n):
    array.append(input())
correcta = input()
saiz = len(correcta)
countMenor = len([1 for l in array if len(l)<saiz])
countIgual = len([1 for l in array if len(l)==saiz])
best = countMenor + (countMenor//k)*5 +1
worst= countMenor + countIgual + ((countMenor+countIgual-1)//k)*5

print(best,worst)
