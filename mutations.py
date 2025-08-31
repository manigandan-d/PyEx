def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

s = input().strip()
pos, ch = input().split()
pos = int(pos)

print(mutate_string(s, pos, ch))
