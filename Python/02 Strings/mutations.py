def mutate_string(string, position, character):
    l1=list(string)
    
    l1[position]=character
    s1="".join(l1)    
    return s1

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
