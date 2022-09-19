import heapq

# find median in a list of integers
class MedianOfAStream:
    max_heap = []  # containing first half of numbers
    min_heap = []  # containing second half of numbers

    def insert_num(self, num):
        # heapq is min_heap, to create a max_heap make each number negative
        # if the number is smaller than the top (largest) number of the max_heap
        if not self.max_heap or -self.max_heap[0] >= num:
            heapq.heappush(self.max_heap, -num)
        # if the number is larger than the top (largest) number of the max_heap
        else:
            heapq.heappush(self.min_heap, num)

        # either both the heaps will have equal number of elements or max-heap will have one
        # more element than the min-heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            # we have even number of elements, take the average of middle two elements
            return -self.max_heap[0] / 2.0 + self.min_heap[0] / 2.0

        # because max-heap will have one more element than the min-heap
        return -self.max_heap[0] / 1.0


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
