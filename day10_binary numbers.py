#!/bin/python3

import math
import os
import random
import re
import sys

def binary(n):
    n = bin(n)[2:]
    res= []
    n = n.split('0')
    for i in n:
        k = str(i.count('1'))
        res.append(int(k))
    return max(res)



if __name__ == '__main__':
    n = int(input().strip())
    print(binary(n))
