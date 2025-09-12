n, x = map(int, input().split())
subjects = [list(map(float, input().split())) for _ in range(x)]

for student in zip(*subjects):
    print(f"{sum(student)/x : .1f}")
