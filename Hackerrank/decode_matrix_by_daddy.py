#!/bin/python3

import math
import os
import random
import re
import sys

def decode_matrix(matrix, row_count, column_count):
    print(matrix)
    decoded_value = ''
    for column_no in range(column_count):
        for row in matrix:
            l_row = row.split()
            decoded_value += l_row[column_no]

    return decoded_value





first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded_matrix = decode_matrix(matrix=matrix, row_count=n, column_count=m)
print(decoded_matrix)
