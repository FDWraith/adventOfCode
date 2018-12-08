with open("input.txt", "r") as f:
    s = f.read().strip()
    f.close()

data = [int(i) for i in s.split(" ")]

total = 0

def parse(d):
    num = d[0]
    meta = d[1]
    
    if num == 0:
        return (2 + meta, d[2:2+meta])
    else:
        meta_vals = []
        leftBound = 2
        for i in range(0, num):
            delta, vals = parse(d[leftBound:])
            leftBound += delta
            meta_vals.extend(vals)
        meta_vals.extend(d[leftBound:leftBound+meta])
        return (leftBound + meta, meta_vals)    

print sum(parse(data)[1])
