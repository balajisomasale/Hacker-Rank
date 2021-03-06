'''
Qn : Multiset Implementation

A  multiset is the same as a set except that an element might occur more than once in a multiset.
Implement a multiset data structure in Python. Given a template for the Multiset class, implement 4 methods:

•	add(self, val): adds val to the multiset
•	remove(self, val): if val is in the multiset, removes val from the multiset; otherwise do nothing
•	_contains_(self, val): returns Tue if val is in the multiset; otherwise return False
•	_len_(self):returns the number of elements in the multiset

Each input file contains several operations, each of one of the  below types. 
Values returned by query and size operations are appended to a result list, which is printed as the output.
•	add val: calls add(val) on the Multiset instance
•	remove val: calls remove(val) on the Multiset instance
•	query val: appends the result of expression val in m, where m is an instance of Multiset and appends the value of that expression to the result list
•	size: calls len(m), where m is an instance of Multiset and appends the returned value to the result list

Complete the class Multiset with the 4 methods given above(add,remove, _contains_, and _len_)

Sample Case

Input:

12			  ->number of queries, q=12
query 1		-> query parameters = [“query 1”, “add 1”, …..” query 2”, “size”]
add 1
query 1
remove 1
query 1
add 2
add 2
size
query 2
remove 2
query 2
size

Output:

False
True
False
2
True
True
1

Explanation:
There are 12 operations to be performed. Start with an empty multiset: multiset=[].
1. The first operation asks if 1 is present in the multiset. False is appende to the result: result=[False]
2. The second operation adds 1 to multiset: multiset=[1]
3. The third operation asks if 1 is present in the multiset. True is appended to the result: result=[False, True]
4. The fourth operation removes 1 from the multiset: multiset=[]
...........................................................................................................................
11. The eleventh operation asks if 2 is in the multiset. Returns True
12. Finally, the last operation asks for the size of the multiset and the length, 1 is appended to the result. 
Result=[False, True, False, 2, True, True, 1]

Solution here
'''

class Multiset:
    global multiset
    multiset=[]
    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.val=val
        multiset.append(val)
        #print(multiset)
    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        self.val=val
        leng=len(multiset)
        
        if leng!=0 and val in multiset:
            m=multiset[leng-1]
            multiset.remove(val)
            #print(multiset)
        else:
            pass   
    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        self.val=val
        if self.val in multiset:
            return True
        else:
            return False
    
    def __len__(self):
        # returns the number of elements in the multiset
        return len(multiset)

if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = performOperations(operations)
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
