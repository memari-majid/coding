"""
longest substrings with no more than k distinct characters
"""


def f(arr,k):
    window_start = 0
    max_length = 0
    distinct_chars = {}
    for window_end in range(len(arr)):
        right_char = arr[window_end]
        if right_char not in distinct_chars:
            distinct_chars[right_char] = 0
        distinct_chars[right_char] += 1
        # number of distinct chars > k
        while len(distinct_chars) > k:
            left_char = arr[window_start]
            distinct_chars[left_char] -= 1
            if distinct_chars[left_char] == 0:
                del distinct_chars[left_char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

arr = "cbbebi"
k = 3
print(f(arr,k))

