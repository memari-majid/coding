nums1 = [1, 2, 3, 7, 0, 0]
nums2 = [5, 6]

# index of last element
p1 = 3 # 5
p2 = 1 # 1

for i in range(5,-1,-1):
    # when read form nums1
    if p2 < 0 or nums2[p2] < nums1[p1]:
        nums1[i] = nums1[p1]
        p1 -= 1
    # when read form nums2
    else:
        nums1[i] = nums2[p2]
        p2 -= 1
