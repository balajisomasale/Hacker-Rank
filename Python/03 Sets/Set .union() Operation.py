# Enter your code here. Read input from STDIN. Print output to STDOUT

n=input()
students = set(map(int,input().split()))

b=input()
b1=set(map(int,input().split()))


print(len(students.union(b1)))

