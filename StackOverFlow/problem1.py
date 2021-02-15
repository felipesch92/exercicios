def calcula(num):
    s_num = str(num)
    s = 0
    for x in range(len(s_num)):
        s += int(s_num[x])
        if x != len(s_num) - 1:
            print(s_num[x], end=' + ')
        else:
            print(s_num[x], end=' = ')
    print(s)
    if len(str(s)) > 1:
        calcula(s)


calcula(493193)
