#!/usr/bin/env python3
from math import  sqrt,gcd
def factorss(n):
	fact=[]
	check=2
	rootn=sqrt(n)
	while check<rootn:
		if n%check==0:
			fact.append(check)
			fact.append(n//check)
		check+=1
	if rootn==check:
		fact.append(check)
	fact.sort()
	if(not fact):
		fact=[n]
	return fact

primes = [2	,3	,5	,7	,11	,13	,17	,19	,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317]
def factors(n):
	counter =0
	res=[]
	while n>1 and counter < len(primes):
		if(n%primes[counter]==0):
			res.append(primes[counter])
			n = n//primes[counter]
		else:
			counter+=1
		if counter == len(primes):
			res.append(n)
	return res
#main
n = int(input())
numbers = list(map(int, input().split()))
nums = {}
sols = []

for i in numbers:
	nums[i]=0
	for k in nums:
		if(k == i):
			continue
		if(gcd(k,i)==1):
			nums[i]+=1
			nums[k]+=1
if(list(nums.keys())==[1]):
	print(1)
	quit()
miniCosa = min(nums, key=lambda k: nums[k])
minLen= nums[miniCosa]
miniLens=[l for l in nums if nums[l] == minLen]
primeDecomposition=[]
for mini in miniLens:
	for i in  factors(mini):
		if i not in primeDecomposition:
			primeDecomposition.append(i)
sol=0
for p in primeDecomposition:
	num=sum([1 for i in numbers if i%p==0])
	if(sol<num):
		sol=num
print(sol)
print("Otra sol")
t=max(numbers)
k=[0]*(t+2)
