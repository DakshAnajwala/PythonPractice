#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    result = ''
    uncap_name = s
    s = s.split(" ")
    for name in s:
        name_0 = name[0].capitalize()
        result = result + name_0
        result = result + name[1:]
        if len(uncap_name) != len(result):
            result = result + " "
        else:
            break

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
    print(result)
