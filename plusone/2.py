def myfunc(l):
    for i in reversed(range(len(l))):
        if l[i] != 9:
            l[i] += 1
            return l
        elif i == 0:
            if l[0] == 9:
                l[i] = 0
                l.insert(0,1)
        elif l[i] == 9:
            l[i] = 0
    return l



l = [1, 9, 9]
resutl = myfunc(l)
print(resutl)

