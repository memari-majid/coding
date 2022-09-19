nums1 = [1, 2, 3, 4, 0, 0]
nums2 = [5, 6]

n = len(nums2) # n = 2
m = len(nums1) - n # m = 4, m+n = 6

nums1_copy = nums1[:m] # = [1, 2]

p1 = 0 # [0,1,2,3]
p2 = 0 # [0,1]

for i in range(n + m):
    # p2 >= 2
    if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
        nums1[i] = nums1_copy[p1]
        p1 += 1
    # p2 < 2
    else:
        nums1[i] = nums2[p2]
        p2 += 1

