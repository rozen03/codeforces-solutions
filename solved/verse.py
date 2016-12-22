#!/usr/bin/env python3
lines = int(input())
patterns = input().split()
textos = []
vocales = "aeiouy"
for i in range(lines):
    textos.append(input())
for i in range(lines):
    contador=0
    for l in textos[i]:
        if (l in vocales):
            contador+=1

    if (contador != int(patterns[i])):
        print("NO")
        exit()
print("YES")
