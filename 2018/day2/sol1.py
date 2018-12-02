with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

def appearances(s):
    '''generates a dictionary of number of times each letter appears in the string'''
    d = {}
    for letter in s:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1 
    return d


twice = 0
thrice = 0
for line in lines:
    appearance = appearances(line)
    if 2 in appearance.values():
        twice += 1
    if 3 in appearance.values():
        thrice += 1
 
print twice * thrice
