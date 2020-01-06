#!/usr/bin/env python3

import math


def fac_bench(n):
    return sum(math.factorial(i) for i in range(1, n))


print(fac_bench(3001), end='')
