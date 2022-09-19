import numpy as np


def multiply(mat1, mat2):
    def compress_matrix(matrix):
        rows, cols = len(matrix), len(matrix[0])
        compressed_matrix = [[] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]:
                    compressed_matrix[row].append([matrix[row][col], col])
        return compressed_matrix

    # Store the non-zero values of each matrix.
    A = compress_matrix(mat1)
    B = compress_matrix(mat2)

    ans = [[0] * len(mat1[0]) for _ in range(len(mat1))]

    for i in range(len(mat1)):
        for element1, k in A[i]:
            for element2, j in B[k]:
                ans[i][j] += element1 * element2
    return ans


if __name__ == "__main__":
    i, k, j = 2, 3, 4
    mat1 = np.random.randint(2, size=(i, k))
    mat2 = np.random.randint(2, size=(k, j))
    result = multiply(mat1, mat2)
    print(result)
