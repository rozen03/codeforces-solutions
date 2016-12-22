#!/usr/bin/env python3
global n,m,t

def recur(caminos,path,tiempoHecho,caminoHecho):
    global n,m,t
    mejorCamino=[]
    mejorTiempo=0
    for i in range(caminos):
        indice=i[0]
        tiempoHecho=+i[1]
        caminoHecho = [0]
        if (tiempoHecho <t or indice not in caminoHecho or indice <n-1):
            caminoHecho.append(indice)
            indice=paths[indice][0]
            tiempoHecho=paths[indice][1]
            recur(path[indice], path, tiempoHecho, caminoHecho)
        #if(len(mejorCamino)<len(caminoHecho)):
        #    mejorCamino=caminoHecho
        return tiempoHecho,caminoHecho


(n,m,t) = input().split()
n =int(n)
paths =[[] for i in range(n)]
m=int(m)
t=int(t)
for i in range(m):
    (a,b,c) = input().split()
    paths[int(a)-1].append((int(b)-1,int(c)))
caminoHecho=[]
tiempoHecho=0
mejorCamino=[]
mejorTiempo=0
indice=0
print(mejorCamino)
