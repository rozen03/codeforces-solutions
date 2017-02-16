#!/usr/bin/env python3
n,m = tuple(map(int, input().split()))
poland = [input() for i in range(n)]
enemy  = [input() for i in range(m)]
cantRepeated = sum ([1 for i in poland if i in enemy])
popo = len(poland)
enen = len(enemy)
if(cantRepeated%2==0):
	if(popo > enen):
		print("YES")
	else:
		print("NO")
	quit()
#else
popo+=1
if(popo > enen):
	print("YES")
else:
	print("NO")
quit()
