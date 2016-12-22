#!/usr/bin/env python3

(c,d) =input()#sys.argv[1]
#c = sys.argv[1][0]
#d=sys.argv[1][1]
moves = [1 for i in range(8)]
#012
#7x3
#654
if c == 'a':
	moves[0] =0
	moves[7] =0
	moves[6] =0
elif c=='h':
	moves[2] =0
	moves[3] =0
	moves[4] =0

if d=='1':
	moves[0] =0
	moves[1] =0
	moves[2] =0
elif d=='8':
	moves[4] =0
	moves[5] =0
	moves[6] =0
print (sum(moves))