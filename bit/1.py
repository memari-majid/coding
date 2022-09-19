def addBinary(a, b):
    return '{0:b}'.format(int(a, 2) + int(b, 2))

a = "1010"
b = "1011"
result = addBinary(a,b)
print(result)