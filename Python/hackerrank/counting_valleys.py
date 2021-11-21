#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    count =0
    total=0
    valleys = []
    for step in path:
        if step == "U":
            count += 1
            valleys.append(count)
        else:
            count += -1
            valleys.append(count)
    print(valleys)
    for x in range(steps):
        if (valleys[x]) == 0 and (valleys[x-1]) < 0:
            total+=1
    return total


if __name__ == '__main__':

    print(countingValleys(8, "UDDDUDUU"))