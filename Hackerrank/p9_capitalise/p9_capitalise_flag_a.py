#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    # is_first_char_after_space = False
    was_space_flag = True
    result = ''
    for c in s:
        if c == ' ':
            was_space_flag = True
            result = result + c
        elif was_space_flag:
            result = result + c.capitalize()
            was_space_flag = False
        else:
            result = result + c

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
    print(result)
