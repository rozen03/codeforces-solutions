#!/bin/bash
reset
rm test
g++ 742B.cpp -fstack-protector-all -g -std=c++14 -O3 -Ofast -fpermissive  -o test
#g++ 740A.cpp -std=c++14   -o test
