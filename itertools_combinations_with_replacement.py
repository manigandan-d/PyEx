from itertools import combinations_with_replacement 

S, k = input().split()
k = int(k)

S = sorted(S)

for comb in combinations_with_replacement(S, k):
    print("".join(comb))
