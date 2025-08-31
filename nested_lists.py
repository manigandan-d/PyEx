students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

scores = sorted(set([s[1] for s in students]))
second_lowest = scores[1]

result = [s[0] for s in students if s[1] == second_lowest]

for name in sorted(result):
    print(name)
