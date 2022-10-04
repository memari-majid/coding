from heapq import *


def find_Kth_smallest_number(nums, k):
    n = len(nums)
    max_heap = []
    # sort k elements
    for i in range(k):
        heappush(max_heap, -nums[i])
    # if there are elements smaller than largest in max-heap
    for i in range(k, n):
        if nums[i] < -max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])

    return -max_heap[0]


print(find_Kth_smallest_number([1, 2, 3, 4, 5, 6], 4))

