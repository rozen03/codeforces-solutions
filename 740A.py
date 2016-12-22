#!/usr/bin/env python3
n,a,b,c = tuple(map(int, input().split()))
resto = n%4;
if (resto==0):
    print(0)
    quit()

if(resto ==2):
    mincho =min(2*a,b)
    mincho = min(mincho,2*c)
    mincho= min(mincho,a+b+c)
elif(resto==1):
    mincho = min(3*a,c)
    mincho= min(mincho,a+b)
    mincho= min(mincho,a+2*b+c)
else:
    mincho=min(a,b+c)
    mincho=min(mincho,3*c)
print(mincho)
