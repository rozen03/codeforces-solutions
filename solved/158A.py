#!/usr/bin/env python3
n,k= tuple(map(int, input().split()))
nums = list(map(int, input().split()))

print(sum(1 for m in nums if m>0 and m>=nums[k-1]))
#val=k
#for i in nums[k:]:
#    if i==nums[k-1]:
#        val+=1
#    else:
#        break
#print(val)
