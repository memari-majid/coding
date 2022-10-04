def two_sum(mylist, target):
    mydict = {}
    for index in range(len(mylist)):
        # mylist[index] = pointer 1
        # complement = pointer fibonacci.py
        complement = target - mylist[index]
        if complement in mydict and mydict[complement] != index:
            return [index,mydict[complement]]
        else:
            mydict[mylist[index]] = index


mylist = [2,7,11,15]
result = two_sum(mylist, 9)
print(result)