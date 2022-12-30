t=int(input())


for i in range(t):
    a,b=input().split()
    #b=int(input())

    try:
        print(int(a) // int(b))
    
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")
    except ValueError as v:
        print(f"Error Code: {v}")
