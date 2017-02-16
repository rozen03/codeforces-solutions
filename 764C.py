#!/usr/bin/env python3
n = int(input())
color,adjas=range(2)
muertos=[]
nodos = {}
for i in range(n):
	nodos[i] = [-1,[]]
for i in range(n-1):
	u,v = tuple(map(int, input().split()))
	u-=1
	v-=1
	nodos[u][adjas].append(v)
	nodos[v][adjas].append(u)
colores=list(map(int, input().split()))
for i,c in enumerate(colores):
	nodos[i][color] = c
posiblesRaices = []
hojas=[(indice,nodo) for indice,nodo in nodos.items() if len(nodo[adjas])<2  and nodo[color] == nodos[nodo[adjas][0]]]
while(hojas):
	for indice,hoja in hojas:
			del(nodos[indice])
	hojas=[(indice,nodo) for indice,nodo in nodos.items() if len(nodo[adjas])<2  and nodo[color] == nodos[nodo[adjas][0]]]

posibleRes=-1
for indice,nodo in [(indice,nodo) for indice,nodo in nodos.items() if len(nodo[adjas])>1]:
	if nodo[color] not in [nodos[i][color] for i in nodos[indice][adjas] ]:
		if(posibleRes==-1):
			posibleRes=indice
		else:
			print("NO")
			quit()

print("YES")
if posibleRes==-1:
	print(1)
else:
	print(posibleRes+1)
