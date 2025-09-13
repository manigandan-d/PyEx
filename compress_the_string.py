from itertools import groupby 

S = input().strip()

result = []

for key, group in groupby(S):
    count = len(list(group))
    result.append((count, int(key)))

print(*result)
