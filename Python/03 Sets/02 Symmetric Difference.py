c = a.difference(b)
d = b.difference(a)

# Union of difference
e = c.union(d)

# Converting set to a list
RESULT = list(e)

# Sorting
RESULT.sort()

# Iteration
for i in range(len(RESULT)):
    print(RESULT[i])
