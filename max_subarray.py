def max_subarray(mylist):
    current = final = mylist[0]
    for number in mylist:
        current = max(number, current + number)
        final = max(final, current)
    return final
