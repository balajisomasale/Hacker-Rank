#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    for index in range(0,len(arr)):
        
        # [4,3,2,1]
        print(str(arr[len(arr)-index-1])+" ",end='')
