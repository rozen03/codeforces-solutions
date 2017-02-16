#!/usr/bin/env python3

def foo(n):
	if(n==1):
		print(3)
		quit()
	if(n==2):
		print(4)
		quit()
	if (n%2==1):
		print(1)
	else:
		print(n-2)
a = int(input())
foo(a)
