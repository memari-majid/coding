def isValid(s):
    # dict lookup by key
    # key = value
    mydict = {')': '(', ']': '[', '}': '{'}
    mystack = []
    for char in s:
        # char is closing
        if char in mydict:
            # top = opening
            if mystack:
                # if stack is not empty we get a top
                top = mystack.pop()
            else:
                # if stack is empty we need a top = not compatible
                top = '#'
            # mydict[closing] == opening
            if mydict[char] != top:
                return False
        # char is opening
        else:
            mystack.append(char)
    return not mystack
