import numpy as np

i = k = j = 2
x1 = np.random.random(size=(i, k))
x2 = np.random.random(size=(k, j))
result = np.zeros(shape=(i, j))
for i in range(len(x1)):
    for j in range(len(x2[0])):
        for k in range(len(x1[0])):
            if (x1[i][k] != 0) and (x2[k][j] != 0):
                result[i][j] += x1[i][k] * x2[k][j]
