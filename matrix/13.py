import numpy as np

mat1 = np.random.randint(2,size=(2,2))
mat2 = np.random.randint(2,size=(2,2))


def multiply(mat1,mat2):

    def compress(mat):
        compressed_matrix = {}
        for i in range(len(mat)):
            for k in range(len(mat[0])):
                if mat[i][k] != 0:
                    # key = (i,j), value = value
                    compressed_matrix[(i, k)] = mat[i][k]
        return compressed_matrix

    compressed_mat1 = compress(mat1)

    ans = np.zeros(len((mat1),len(mat2[0])))

    for i,k in compressed_mat1.keys():
        for j in range(len(mat2[0])):
            if mat2[k][j]:
                ans[i][j] += compressed_mat1[(i,k)] * mat2[k][j]

    return ans






