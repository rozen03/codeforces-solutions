#!/usr/bin/env python3
n = int(input())
ids= list(map(int, input().split()))
ids = [i-1 for i in ids]
id_tree= [0]*n
maxx=0
for k,i in enumerate(ids):
	if (id_tree[i]==0 and id_tree[k]==0 ):
		maxx+=1
		id_tree[i]=maxx
		id_tree[k]=maxx
	elif(id_tree[i]==0):
		id_tree[i]=id_tree[k]
	else:
		id_tree[k]=id_tree[i]
print(maxx)
