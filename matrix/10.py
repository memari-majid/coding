"""
sparse matrix multiplication
"""

# check if matrix 1 column == matrix 2.py row
def sparse_matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return[[]]

    sparse_a = get_dict_of_nonzero_cells(matrix1)
    sparse_b = get_dict_of_nonzero_cells(matrix2)

    matrix3 = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    # matrix-1 row and col

    # iterate through mat1 row and col
    for i, k in sparse_a.keys():
        # matrix-2.py column
        for j in range(len(matrix2[0])):
            # matrix-2.py col
            if (k,j) in sparse_b.keys():
            #if matrix2[k][j] != 0:
                matrix3[i][j] += sparse_a[(i,k)] * sparse_b[(k,j)]
    return matrix3


def get_dict_of_nonzero_cells(matrix):
    dict_of_nonzero_cells = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                # key = (i,j), value = value
                dict_of_nonzero_cells[(i,j)] = matrix[i][j]
    return dict_of_nonzero_cells