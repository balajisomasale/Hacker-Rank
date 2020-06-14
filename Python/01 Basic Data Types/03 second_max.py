'''
Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.

'''


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    res=0
    l1=list(arr)
    m1=max(l1)
    
    while m1==(max(l1)):
        l1.remove(m1)
    l2=max(l1)
    print(l2)
