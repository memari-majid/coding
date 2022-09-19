from heapq import *


def find_Kth_smallest_number(nums, k):
    max_heap = []
    for i in range(k):
        heappush(max_heap, -nums[i])
    for i in range(k, len(nums)):
        if nums[i] < -max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])

    return -max_heap[0]


print(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3))

print(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4))

print(find_Kth_smallest_number([5, 12, 11, -1, 12], 3))
