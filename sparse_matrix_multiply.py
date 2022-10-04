import numpy as np


def sparse_multiply(mat1, mat2):
    def compress(mat):
        compressed_mat = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    compressed_mat[(i, j)] = mat[i][j]
        return compressed_mat

    compressed_mat1 = compress(mat1)
    compressed_mat2 = compress(mat2)
    ans = np.zeros(shape=(len(mat1), len(mat2[0])))

    for i, k in compressed_mat1:
        for j in range(len(mat2[0])):
            if (k, j) in compressed_mat2.keys():
                ans[i][j] += compressed_mat1[(i, k)] * compressed_mat2[(k, j)]
    return ans


if __name__ == '__main__':

    i, k, j = 2, 3, 4
    mat1 = np.random.randint(2, size=(i, k))
    mat2 = np.random.randint(2, size=(k, j))
    ans = np.zeros(shape=(i, j))

    for i in range(len(mat1)):
        for k in range(len(mat1[0])):
            for j in range(len(mat2[0])):
                ans[i][j] += mat1[i][k] * mat2[k][j]

    ans2 = sparse_multiply(mat1, mat2)

    if (ans == ans2).all:
        print(True)
