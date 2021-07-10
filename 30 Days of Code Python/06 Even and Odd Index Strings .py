# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    name=str(input())
    mylist=list(name)
    
    result=("".join(mylist[::2]))
    result2=("".join(mylist[1::2]))
    print(result+" "+result2)
        
        
       
            
        
          
        
    