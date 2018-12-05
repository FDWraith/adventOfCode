with open("input.txt", "r") as f:
    s = f.read().strip()
    f.close()

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

print len("".join(stack))
    
