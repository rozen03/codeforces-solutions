#!/usr/bin/env python3
b = input()
a = input().split()
vector = [int(i) for i in a]
print(vector)

def getDist(vector, entero):
	contador =0
	for i in vector:
		coso = i - entero
		if (coso <0):
			coso = (-1)*coso
		contador+= coso
	return contador


vector= sorted(vector)
indice=int(len(vector)/2)