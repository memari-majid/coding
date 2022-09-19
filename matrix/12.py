import numpy as np

mat1 = np.random.random(size=(3,4))
mat2 = np.random.random(size=(4,2))
mat3 = np.zeros(shape=(len(mat1),len(mat2[0])))

# result = [[0] * len(mat2[0]) for _ in range(len(mat1))]
# result = []
# for i in range(len(mat1)):
#     result.append([0] * len(mat2[0]))
