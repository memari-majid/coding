# all combinations of list of lists
# The list  must be created once and out of the recursive function
mylist = []
def getAllCombinations(next, previous):
    # check if next is last element in the inner list
    last_element = (len(next) == 1)
    # iterate through the elements of the inner list
    for i in range(len(next[0])):
        new = previous + next[0][i]
        # if last element in the inner list
        if last_element:
            # stop the iteration and add the list
            mylist.append(new)
        else:
            # if not last continue the iteration
            getAllCombinations(next[1:], new)
    return mylist

s= [['A'], ['B', 'C', 'D'], ['E', 'F']]
# start with an empty string ''
result = getAllCombinations(s, '')
print(result)
