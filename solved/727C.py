#!/usr/bin/env python3
import sys
n = int(input())
arr={}
print("?",1,2)
sys.stdout.flush()
a= int(input())
print("?",1,3)
sys.stdout.flush()
b=int(input())
print("?",2,3)
sys.stdout.flush()
c=int(input())

arr[1]=(b+a-c)//2
arr[2]=a-arr[1]
arr[3]=b-arr[1]
for i in range(4,n+1):
    print("?",1,i)
    sys.stdout.flush()
    arr[i]=int(input()) -arr[1]
print("!", str.join(" ", [str(i) for i in arr.values()]))
