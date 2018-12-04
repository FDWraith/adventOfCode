'''
Idea:

Use a dictionary structure:
 - Keys: Guard ID
 - Values: Array, representing the 60 min interval of 00 - 59. Values of array represent how often guard fell asleep
'''

with open("sortedInput.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    f.close()


guard_sleep_table = {}

currentGuard = None
leftBound = 0
for line in lines:
    line = line.split(" ")
    if line[2] == "Guard":
        currentGuard = int(line[3][1:])
        if currentGuard not in guard_sleep_table:
            guard_sleep_table[currentGuard] = [0 for i in range(0,60)]
    else:
        if line[2] == "falls":
            leftBound = int(line[1].split(":")[1][:-1])
        else:
            rightBound = int(line[1].split(":")[1][:-1])
            # mark the times that the guard was asleep for
            for i in range(leftBound, rightBound):
                guard_sleep_table[currentGuard][i] += 1

# testing purposes
print guard_sleep_table
