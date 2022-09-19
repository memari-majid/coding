def f(arr):
    p1 = 0
    p2 = 1
    while p2+1 < len(arr):
        if arr[p1] != arr[p2]:
            arr[p1+1] = arr[p2]
            p1 += 1
        p2 += 1
    return p1+1


arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(f(arr))
print(arr)