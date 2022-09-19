def find_subsets(arr):
    subsets = [[]]
    # for each element
    for element in arr:
        # for each subset
        for i in range(len(subsets)):
            new_subset = list(subsets[i])
            # add the current element to each subset
            new_subset.append(element)
            # add the subset to the subsets
            subsets.append(new_subset)
    return subsets



print(find_subsets([1, 3]))
print(find_subsets([1, 5, 3]))



