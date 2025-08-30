T = int(input())

for _ in range(T):
    try:
        a, b = input().split()
        
        a, b = int(a), int(b)
        
        print(a // b)

    except ZeroDivisionError as e:
        print("Error Code:", e)

    except ValueError as e:
        print("Error Code:", e)
