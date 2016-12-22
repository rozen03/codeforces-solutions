#!/usr/bin/env python3
n,m= tuple(map(int, input().split()))
lista = [list(map(int, input().split())) for _ in range(n)]
for k,numeros in enumerate(lista):
    contadur=0
    for i,n in enumerate(numeros):
        if n!=(i+1):
            print(contadur)
            if contadur<k+2:
                contadur+=1
            else:
                print("NO")
                quit()
print("YES")
