with open("input.txt", "r") as f:
    s = f.read().strip()
    f.close()


def polymer_len(s):
    stack = [""]
    for char in s:
        if char.islower():
            if char == stack[-1].lower() and stack[-1].isupper():
                stack = stack[:-1]
            else:
                stack.append(char)
        else:
            if char == stack[-1].upper() and stack[-1].islower():
                stack = stack[:-1]
            else:
                stack.append(char)
    return len("".join(stack))

def removeAll(s, c):
    s = s.replace(c.upper(), "")
    s = s.replace(c.lower(), "")
    return s

minLen = polymer_len(s)
for letter in "abcdefgheijklmnopqrstuvwxyz":
    l = polymer_len(removeAll(s, letter))
    if l < minLen:
        minLen = l

print minLen
