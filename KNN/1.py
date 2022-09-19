import math
import numpy as np


def distance(v1, v2):
    d = 0.0
    for i in range(len(v1)):
        d += (v1[i] - v2[i]) ** 2
    return math.sqrt(d)


def get_neighbors(dataset, v1, num_neighbors):
    distances = []
    for v2 in dataset:
        d = distance(v1, v2)
        distances.append((v2, d))
    distances.sort(key=lambda row: row[1])
    neighbors = []
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors


if __name__ == '__main__':
    dataset = np.random.random(size=(10, 4))
    neighbors = get_neighbors(dataset, dataset[0], 3)
    print(neighbors)
