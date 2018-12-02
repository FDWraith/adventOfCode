with open("input1.txt","r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    f.close()

sum = 0
for line in lines:
    if line[0] == "+":
        sum += int(line[1:])
    else:
        sum -= int(line[1:])

print sum
