"""
regular matrix multiplication
"""
def multiply( mat1, mat2) :
    # initialize the output size
    ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]
    # iterate through mat1 rows
    for row_index, row_elements in enumerate(mat1):
        # iterate through row elements
        for element_index, row_element in enumerate(row_elements):
            # 0 == False
            if row_element:
                for col_index, col_element in enumerate(mat2[element_index]):
                    ans[row_index][col_index] += row_element * col_element

    return ans