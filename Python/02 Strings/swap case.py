def swap_case(s):
    r=[]
    for i in s:
        # print(i)
        if i.isupper():
            r.append(i.lower())
            
        else:
            r.append(i.upper())
            #r.append(i)
    return "".join(r)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
