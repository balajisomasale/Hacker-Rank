# input the number of test cases 
# Outpput True or False if the regex expression is valid or not 

# # sample input : 
# 2
# .*\+
# .*+


import re

for _ in range(int(input())):
    try:
        a = re.compile(input())
        print("True")
    except Exception:
        print("False")
