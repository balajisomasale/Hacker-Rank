n=input()
n1 = set(map(int,input().split()))

b=input()
b1=set(map(int,input().split()))

union1=n1.union(b1)
intersection1= n1.intersection(b1)

print(len(union1-intersection1))


# or second solution 
# print(len(n1.symmetric_difference(b1)))
