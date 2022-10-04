def romanToInt(s):
    mydict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    while i < len(s):
        # subtractive
        if i + 1 < len(s) and mydict[s[i]] < mydict[s[i + 1]]:
            total += mydict[s[i + 1]] - mydict[s[i]]
            i += 2
        else:
            total += mydict[s[i]]
            i += 1

    return total


if __name__ == '__main__':
    s = "MCMXCIV"
    print(f'MCMXCIV = {romanToInt(s)}')
