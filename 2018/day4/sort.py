import datetime

def sort_key(s):
    s = s[1:17]
    vals = s.split(' ')
    vals = vals[0].split('-') + vals[1].split(":")
    vals = [int(val) for val in vals]
    return datetime.datetime(vals[0], vals[1], vals[2], vals[3], vals[4])


with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    f.close()

with open("sortedInput.txt", "w") as f:
    lines = sorted(lines, key = sort_key)
    for line in lines:
        f.write(line + "\n")
    f.close()

