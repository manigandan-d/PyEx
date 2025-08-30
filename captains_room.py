from collections import Counter

K = int(input())
room_list = list(map(int, input().split()))

counts = Counter(room_list)

print(counts)

for room, freq in counts.items(): 
    if freq == 1: 
        print(room)
        break
