with open("input.txt","r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    f.close()

sum = 0
seen = set([0])
exit = False

while exit == False:
    for line in lines:
        if line[0] == "+":
            sum += int(line[1:])
        else:
            sum -= int(line[1:])
    
        if sum in seen:
            print sum
            exit = True
            break
        else:
            seen.add(sum)

