#!/usr/bin/env python3
palabra = input().lower()
nuevaPalabra=""
for p in palabra:
    if p in "aiueoy":
        continue
    nuevaPalabra+="."+p
print(nuevaPalabra)
