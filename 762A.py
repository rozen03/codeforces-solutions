#!/usr/bin/env python3
from math import  sqrt
n,k = tuple(map(int, input().split()))
counter=0
res=0
for i in range(1,sqrt(n)+1):
	if n%i==0:
		counter+=1
		res=i
	if counter==k:
		break
if counter==k:
	print(res)
	quit()
counter+=1
if counter==k:
	print(n)
else:
	print(-1)
