#!/usr/bin/env python3
n = int(input())
palabras = [input() for _ in range(n)]
for palabra in palabras:
    if(len(palabra)<11):
        print(palabra)
        continue
    print(palabra[0]+str(len(palabra[1:-1]))+palabra[-1])
