import heapq

"""
We maintain two heaps in the following way:
    A max-heap to store the smaller half of the input numbers
    A min-heap to store the larger half of the input numbers
Both the heaps are balanced (or nearly balanced)
The max-heap contains all the smaller numbers while the min-heap contains all the larger numbers
"""


class MedianOfAStream:
    max_heap = []  # containing first half of numbers
    min_heap = []  # containing second half of numbers

    def insert_num(self, num):
        # heapq by default is a min_heap, to create a max_heap make each number negative
        # if the max heap is empty or the number is smaller than the top (largest) number of the max_heap
        # push the number to max_heap
        if self.max_heap is None or -self.max_heap[0] >= num:
            heapq.heappush(self.max_heap, -num)
        # if the number is larger than the top (largest) number of the max_heap
        # push the number to min_heap
        else:
            heapq.heappush(self.min_heap, num)

        # either both the heaps will have equal number of elements or max-heap have one
        # more element than the min-heap, pop from max_heap and push to min_heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        # we have an even number of elements, take the average of middle two elements
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        # because max_heap always have one more element than the min_heap
        # the middle number is the top element of max_heap
        return -self.max_heap[0] / 1.0


def main():
    median_of_a_stream = MedianOfAStream()
    median_of_a_stream.insert_num(3)
    median_of_a_stream.insert_num(1)
    print("The median is: " + str(median_of_a_stream.find_median()))
    median_of_a_stream.insert_num(5)
    print("The median is: " + str(median_of_a_stream.find_median()))
    median_of_a_stream.insert_num(4)
    print("The median is: " + str(median_of_a_stream.find_median()))


main()
