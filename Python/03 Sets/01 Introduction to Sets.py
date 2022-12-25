def average(array):
    # your code goes here
    count=0
    n1=0
    s1=set(array)
    for item in s1:
        count+=item
        n1+=1
    
    return count/n1
        
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
