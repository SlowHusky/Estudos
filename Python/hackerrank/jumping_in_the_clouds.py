#!/bin/python3
"""https://www.hackerrank.com/challenges/jumping-on-the-clouds"""
import math

import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    count = 0
    end = 0
    while end < len(c)-1:
        if (end < len(c)-2) and (c[end+2] == 0):
            count += 1
            end+=2    
        elif c[end+1] == 0:
            count+=1
            end+=1
    return count

if __name__ == '__main__':
    c = [0,1,0,0,0,1,0]
    print(jumpingOnClouds(c))
    c = [0, 0, 0, 1, 0, 0]
    print(jumpingOnClouds(c))