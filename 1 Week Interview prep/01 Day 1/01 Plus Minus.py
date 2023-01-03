#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    count_positive=0
    count_negative=0
    count_zeros=0
    for i in arr:
        if i>0:
            count_positive+=1
        elif i<0:
            count_negative+=1
        else:
            count_zeros+=1
    
    print(count_positive/len(arr))
    print(count_negative/len(arr))
    print(count_zeros/len(arr))
            
            
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
