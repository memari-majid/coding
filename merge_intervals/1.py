from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


# list of intervals
list_of_intervals = [Interval(1, 3), Interval(5, 7), Interval(8, 12), Interval(4, 6)]


print("list of intervals before merge")
for interval in list_of_intervals:
    interval.print_interval()

print("\nlist of intervals after merge")

# sort the intervals on the start time
list_of_intervals.sort(key=lambda x: x.start)


start = list_of_intervals[3].start
end = list_of_intervals[3].end

for i in range(0, len(list_of_intervals)-1):
    interval = list_of_intervals[i]
    if interval.end < start or interval.start > end:
        continue
    if interval.start <= end:
        end = max(interval.end, end)
        list_of_intervals.append(Interval(start,end))


for interval in list_of_intervals:
    interval.print_interval()

