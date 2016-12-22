#!/usr/bin/env python3

formato = int(input())
hora,minuto = input().split(':')
hora = int(hora)
minuto= int(minuto)
out_hora=""
out_minuto=""
if(formato == 12):
    formato = 13
if(hora>=formato):
   hora -=hora//10*10
if(hora ==0 and formato ==13):
    hora=10
if (minuto>= 60):
    minuto -= minuto//10*10

if (hora <10):
    out_hora+="0"
if (minuto<10):
    out_minuto+="0"
out_hora+=str(hora)
out_minuto+=str(minuto)
print(out_hora+":"+out_minuto)
