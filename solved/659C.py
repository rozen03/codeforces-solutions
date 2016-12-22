#!/usr/bin/python3
n,m= tuple(map(int, input().split()))
lista = list(map(int, input().split()))
res = []
indice=0
i=1
lista= sorted(lista)
while(i <=m):
    if (i<lista[indice]):
        res.append(i)
        m-=i
        if(m==i):
            i = 300*m
        i+=1
    else:
        if(i==lista[indice]):
            i+=1
        indice+=1
        if(indice==len(lista)):
            while(i<=m):
                res.append(i)
                m-=i
                if(m==i):
                    i = 300*m
                i+=1
    #print(m,i,indice,res)
print(len(res))
print(str.join(" ",list(map(str,res))))
#
