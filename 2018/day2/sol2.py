with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    f.close()

def compare(s1, s2):
    differences = 0
    for letterIndex in range(len(s1)):
        if s1[letterIndex] != s2[letterIndex]:
            differences += 1
    return differences

def similar(s1, s2):
    sim = ""
    for letterIndex in range(len(s1)):
        if s1[letterIndex] == s2[letterIndex]:
            sim += s1[letterIndex]
    return sim

for line in lines:
    for line2 in lines:
        if compare(line, line2) == 1:
            print similar(line, line2)
            break
