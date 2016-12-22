#!/usr/bin/env python3
n,m,k= tuple(map(int, input().split()))
pointz=[tuple(map(int, input().split())) for _ in range(k)]


points=list(set(pointz+[(0,i) for i in range(m+1)]+[(n,i) for i in range(m+1)]+[(i,0) for i in range(n+1)]+[(i,m) for i in range(n+1)]))
blah=[{},{}]
for i in range(-m+1,n):
    #blah[0][i]=sorted([(p[0]-i,p) for p in points if p[1]-p[0]==-i and p[0]-i >0])
    #blah[1][i]=sorted([(i -p[0],p) for p in points if p[1]+p[0]==i])
    blah[0][i]=sorted([p for p in points if p[1]-p[0]==-i and p[0]-i >0])
    blah[1][i]=sorted([p for p in points if p[1]+p[0]==i])
print(blah)
pasos=blah[0][0][0][0]
indice=blah[0][0][0][0]
direction=1
diccc = 0
punto=blah[0][0][0]
secwencia =[punto]
#ultimo=blah[0][0][0]
x=punto[0]
val=0
while(punto not in [(0,0),(0,m),(n,0),(n,m)]):
    if(punto[1]==0):
        direction=1
        val=punto[0]
    elif(punto[1]==m):
        direction=-1
        val=punto[0]
    if(punto[0]==0):
        diccc = 0
        val=punto[0]
    if(punto[0]==n):
        diccc = 1
        val=punto[0]
    print(diccc,val)
    wut= blah[diccc][val].index(punto)
    punto=blah[diccc][val][wut+direction]
    secwencia+=[punto]
    x+=direction
    #blah[diccc][]
print(secwencia)
