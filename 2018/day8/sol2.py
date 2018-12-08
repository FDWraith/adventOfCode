with open("input.txt", "r") as f:
    s = f.read().strip()
    f.close()

data = [int(i) for i in s.split(" ")]

total = 0

def parse(d):
    num = d[0]
    meta = d[1]
    
    if num == 0:
        return (2 + meta, sum(d[2:2+meta]))
    else:
        vals = []
        leftBound = 2
        total = 0
        for i in range(0, num):
            delta, val = parse(d[leftBound:])
            leftBound += delta
            vals.append(val)

        for i in range(0, meta):
            meta_val = d[leftBound+i] - 1
            if meta_val < len(vals):
                total += vals[meta_val]
        print vals
        return (leftBound + meta, total)    

print parse(data)
