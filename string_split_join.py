def split_and_join(line):
    return "-".join(line.split(" "))

line = input().strip()

print(split_and_join(line))
