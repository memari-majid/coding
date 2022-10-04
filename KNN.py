import math
import numpy as np


def distance(vector1, vector2):
    d = 0.0
    for i in range(len(vector1)):
        d += (vector1[i] - vector2[i]) ** 2
    return math.sqrt(d)


def get_neighbors(dataset, vector1, num_of_neighbors):
    d_from_vector1 = []
    for vector2 in dataset:
        d = distance(vector1, vector2)
        d_from_vector1.append((vector2, d))
    # sort based on distance
    d_from_vector1.sort(key=lambda row: row[1])
    vector1_neighbors = []
    for i in range(num_of_neighbors):
        vector1_neighbors.append(d_from_vector1[i])
    return vector1_neighbors


if __name__ == '__main__':
    dataset = np.random.random(size=(10, 4))
    neighbors = get_neighbors(dataset, dataset[0], 3)
    for vectors in neighbors:
        print(vectors)