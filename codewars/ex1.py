def tribonacci(signature, n):
    res = []
    p = signature[0]
    s = signature[1]
    t = signature[2]
    if n == 0:
        res = []
    elif n == 1:
        res.append(p)
    elif n == 2:
        res.append(p)
        res.append(s)
    elif n == 3:
        res.append(p)
        res.append(s)
        res.append(t)
    else:
        res.append(p)
        res.append(s)
        res.append(t)
        for x in range(3, n):
            q = t + s + p
            res.append(q)
            p = s
            s = t
            t = q
    print(res)


tribonacci([57, 24, 27], 390)
