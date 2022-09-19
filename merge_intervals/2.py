def insert(intervals, new_interval):
    new_list = []
    i = 0
    start = 0
    end = 1
    # skip non overlapping
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        new_list.append(intervals[i])
        i += 1
    print(i)
    # merge overlapping
    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(new_interval[start],intervals[i][start])
        new_interval[end] = max(new_interval[end], intervals[i][end])
        new_list.append(new_interval)
        i += 1
    print(i)
    while i < len(intervals):
        new_list.append(intervals[i])
        i += 1
    print(i)
    return new_list




print(str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
print(str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
print(str(insert([[2, 3], [5, 7]], [1, 4])))



