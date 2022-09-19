def merge(l1, l2):
    m = len(l1)
    n = len(l2)
    l1_copy = l1[:n]
    index1 = 0
    index2 = 0

    # Compare elements from nums1Copy and nums2 and write the smallest to nums1.
    for index in range(n + m):
        # We also need to ensure that index1 and index2 aren't over the boundaries
        # of their respective arrays.
        if index2 >= n or (index1 < m and l1_copy[index1] <= l2[index2]):
            l1[index] = l1_copy[index1]
            index1 += 1
        else:
            l1[index] = l2[index2]
            index2 += 1