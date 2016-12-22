#!/usr/bin/env python3

size=input()
#letras="WBWBBBBWBWBWBWBBW"
letras = input()
arraycontador=[]
arraycontador.append(0)
indicei=0
for l in letras:
    if l=="W":
        if arraycontador[indicei]>0:
            indicei+=1
            arraycontador.append(0)
    else:
        arraycontador[indicei]+=1
if arraycontador[indicei]==0:
    del (arraycontador[indicei])
print(len(arraycontador))
print(''.join(str(e)+" " for e in arraycontador))
