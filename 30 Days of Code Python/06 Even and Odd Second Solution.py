# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    name=str(input())
    mylist=list(name)
    
    a=[];
    b=[];
    
    for index in range(0,len(name)):
        if index%2:
            a.append(name[index]);
            
        else:
            b.append(name[index]);
        
            
    print("".join(b)+(" ") + "".join(a))
    
        
       
    
        
        
       
            
        
          
        
    