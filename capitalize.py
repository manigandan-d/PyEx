def capitalize_name(s):
    return " ".join(word.capitalize() for word in s.split(" ")) 

S = input()

print(capitalize_name(S))
