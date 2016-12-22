#!/usr/bin/env python3
n = int(input())
print(sum([ 1 for i in [sum( list(map(int, input().split()))) for _ in range(n)] if i>1]))
