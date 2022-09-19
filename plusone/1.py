def plus_one(digits):
    n = len(digits)
    for i in range(n):
        idx = n - 1 - i
        # all nines
        if digits[idx] == 9:
            digits[idx] = 0
        else:
            # there's one non-nine
            digits[idx] += 1
            return digits
    # we're here because all the digits are nines
    return [1] + digits


l = [1, 9, 9]
resutl = plus_one(l)
print(resutl)
