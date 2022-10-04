def pascal_tri(n):
    # start from 1
    l = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        # skip first and last element
        for j in range(1, i):
            l[i][j] = l[i - 1][j - 1] + l[i - 1][j]
    return l


print(pascal_tri(5))
