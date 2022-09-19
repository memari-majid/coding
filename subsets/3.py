def find_permutations(arr):
    result = []
    perms = [[]]
    for element in arr:
        for _ in range(len(perms)):
            old_permutation = perms.pop(0)
            # create a new permutation by adding the current number at every position
            for j in range(len(old_permutation) + 1):
                new_perms = list(old_permutation)
                # All the elements after jth are shifted to the right
                new_perms.insert(j, element)
                if len(new_perms) == len(arr):
                    result.append(new_perms)
                else:
                    perms.append(new_perms)

    return result


print((find_permutations([1, 3, 5])))


