#!/usr/bin/env python3
n,m = input().split()
n=int(n)
m=int(m)
points = [input().split() for i in range(m)]
points = [(int(i),int(j)) for i,j in points]
filas = []
columnas=[]
resultados =[]
contador = (n**2)
matriz = [[0 for x in range(n)] for x in range(n)]
k_filas=0
k_columnas=0
for k,(i,j) in enumerate(points):
    esta_i =i in filas
    esta_j=j in columnas
    if contador==72:
        bul = True
    else:
        bul=False
    if (not esta_i):
        print("k_filas=",n-k_filas)
        contador -= n-k_filas
        filas.append(i)
        k_filas+=1
    if (not  esta_j):
        print("n-k_columnas",n-k_columnas)
        contador -= n-k_columnas
        columnas.append(j)
        k_columnas+=1
    if (not esta_i and not esta_j and contador !=0):
        contador+=1
    resultados.append(str(contador))
    #for v,val in enumerate(matriz):
    #    for w,wal in enumerate(matriz[v]):
    #        if v==i-1 or w==j-1:
    #            matriz[w][v]=1
    #for wop in matriz:
    #    print (wop)
    #print("---")

print(str.join(" ",resultados))
