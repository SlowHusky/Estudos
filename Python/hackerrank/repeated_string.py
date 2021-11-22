#!/bin/python3
"""https://www.hackerrank.com/challenges/repeated-string/"""
import math
import os
import random
import re
import sys


def repeat_return(s,n):
    return s.count('a')*n

def repeatedString(s, n):
    # Write your code here
    #calculate string size:
    division = n // len(s)
    rest = n % len(s)
    return repeat_return(s,division) + s[:n % len(s)].count("a")

if __name__ == '__main__':
    print(repeatedString('kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm', 736778906400))