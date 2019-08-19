#!/usr/bin/env python3

from functools import reduce
import operator

def fac(n):
    return reduce(operator.mul, range(1, n+1), 1)

def fac_bench(n):
    return sum(map(fac, range(1, n+1)))

print(fac_bench(3000), end='')
