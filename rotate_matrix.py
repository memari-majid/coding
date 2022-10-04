'''
Rotate a matrix in-place
'''


def rotate_matrix(m):
    n = len(m[0])
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = m[i][j]
            m[i][j] = m[n - 1 - j][i]
            m[n - 1 - j][i] = m[n - 1 - i][n - 1 - j]
            m[n - 1 - i][n - 1 - j] = m[j][n - 1 - i]
            m[j][n - 1 - i] = temp


def printMatrix(m):
    for i in range(len(m[0])):
        print(m[i])


A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
O = [
    [13, 9, 5, 1],
    [14, 10, 6, 2],
    [15, 11, 7, 3],
    [16, 12, 8, 4]
]
rotate_matrix(A)
printMatrix(A)
