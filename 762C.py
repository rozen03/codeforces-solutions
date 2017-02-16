#!/usr/bin/env python3
a=input()
b=input()
if(not b):
	b=input()
output=""
indexA=0
for i in a:
	try:
		indexA= b.index(i,indexA)+1
		output+=i
	except:
		pass
if(output=="" or len(output) ==1):
	print("-")
else:
	print(output)
