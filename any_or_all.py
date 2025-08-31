n = int(input())
numbers = list(map(int, input().split()))

all_positive = all(x > 0 for x in numbers)
any_palindrome = any(str(x) == str(x)[::-1] for x in numbers)

print(all_positive and any_palindrome)
