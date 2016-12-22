from math import sqrt
n,m= tuple(map(int, input().split()))
if (m<= n+1):
    print("-1")
    exit()
res="-1"
if n%2==0 and (m>= n+2):
    res=str(n)+" "+str(n+1)+" "+str(n+2)
elif (m>=n+3):
    res=str(n+1)+" "+str(n+2)+" "+str(n+3)
else:
    if (m<= n+2):
        print("-1")
        exit()
    coso=0
    for i in range(2,n+1):
        if not(n%i) and (n%2):
                coso=i
                break
    if not coso:
        print("-1")
        exit()
    for i in range(n+2,m):
        if i%coso ==0:
            res=res=str(n)+" "+str(n+1)+" "+str(i)
print(res)
