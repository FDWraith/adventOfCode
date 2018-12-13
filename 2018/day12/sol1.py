with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    f.close

head = lines[0].split(": ")[1]
rules = lines[2:]

class Rule(object):
    def __init__(self, rule, res):
        assert len(rule) == 5
        assert isinstance(rule, str)

        self.rule = rule
        self.res = res

    def __str__(self):
        return self.rule
    
    def apply(self, s):
        """
        determines if this rule applies to s
        """
        return self.rule == s
    
    def result(self):
        """
        returns the result of applying this rule
        """
        return self.res


rules = [rule.split(" => ") for rule in rules]
rules = [Rule(rule[0], rule[1]) for rule in rules]



# The starting pot on left is 0
leftIndex = 0 
pots = [c for c in "....."] + [char for char in head] + [c for c in "....."]
counter = 0

while counter < 50000000000:
    print pots, leftIndex
    new_pots = ["." for i in range(len(pots))]
    
    for i in range(2,len(pots) - 2):
        s = "".join(pots[i-2:i+3])
        # print s
        
        ruleApplied = False
        for rule in rules:
            if not ruleApplied and rule.apply(s):
                ruleApplied = True
                new_pots[i] = rule.result()


    leftChange = len("".join(pots).lstrip(".")) - len("".join(new_pots).lstrip("."))
    leftIndex += leftChange    
    new = "".join(new_pots).strip(".")

    prev = "".join(pots).strip(".")
    if prev == new:
        leftIndex += 50000000000 - counter - 1
        break

    pots = [c for c in "....."] + [char for char in new] + [c for c in "....."]
    counter += 1



# Compute plant values
total = 0
v = leftIndex
for c in "".join(pots).strip("."):
    if c == "#":
        total += v
    v += 1

print leftIndex
print total

