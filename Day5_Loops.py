#!/bin/python3

import sys

n = int(input().strip())

for i in range(1,11):
    print("%d x %d = %d" % (n, i, (i*n)))
