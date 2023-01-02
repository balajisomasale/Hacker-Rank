import re
expression=input()
pattern="[^aeiouAEIOU]?([aeiouAEIOU]{2,})[^aeiouAEIOU]"
values=re.findall(pattern,expression)
if len(values)>0:
    for i in values:
        print(i)
else:
    print -1
