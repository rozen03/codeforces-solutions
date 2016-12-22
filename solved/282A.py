#!/usr/bin/env python3
#from itertools import accumulate
from functools import reduce
n = int(input())
res=0
for i in range(n):
    res += (1 if "++" in input() else -1)
print(res)
#print(sum[(1 if "++"in input() else -1) for a in range(n)])
