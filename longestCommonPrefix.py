def LCP(arr):
    shortest = min(arr, key=len)
    for i, ch in enumerate(shortest):
        for word in arr:
            if word[i] != ch:
                return shortest[:i]
    return shortest

arr = ["school", "schedule", "scotland"]

print(LCP(arr))
