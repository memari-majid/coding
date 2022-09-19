def find_subsets(nums):
    # sort the numbers to handle duplicates
    list.sort(nums)
    subsets = [[]]
    start_index, end_index = 0, 0
    for i in range(len(nums)):
        start_index = 0
        if i > 0 and nums[i] == nums[i - 1]:
            start_index = end_index + 1
        end_index = len(subsets) - 1
        for j in range(start_index, end_index + 1):
            new_set = list(subsets[j])
            new_set.append(nums[i])
            subsets.append(new_set)
    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
