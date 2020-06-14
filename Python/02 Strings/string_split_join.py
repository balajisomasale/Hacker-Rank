'''
Sample Input
this is a string   
Sample Output
this-is-a-string

'''

def split_and_join(line):
    # write your code here
    new=line.split()
    res="-".join(new)
    return res

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
