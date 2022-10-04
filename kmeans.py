import random


class Centroid:
    def __init__(self, location):
        self.location = location
        self.closests = set()

def get_k_means(features, num_features, k):
    # Don't change the following two lines of code.
    random.seed(42)
    # Gets the initial users, to be used as centroids.
    initial_centroids = random.sample(sorted(list(features.keys())), k)
    centroids = [Centroid(features[i]) for i in initial_centroids]
    for _ in range(10):
        for i, features in features.items():
            closest_centroid_distance = float('inf')
            closest_centroid = None
            for centroid in centroids:
                features_to_centroid_distance = get_manhatan_distance(features, centroid.location)
                if features_to_centroid_distance < closest_centroid_distance:
                    closest_centroid_distance = features_to_centroid_distance
                    closest_centroid = centroid
                closest_centroid.closests.add(i)

            for centroid in centroids:
                centroid.location = get_centroid_average(centroid, features, num_features)
                centroid.closests.clear()

        return [centroid.location for centroid in centroids]


def get_manhatan_distance(features, other_features):
    absolute_difference = []
    for i in range(len(features)):
        absolute_difference.append(abs(features[i] - other_features[i]))
    return sum(absolute_difference)

def get_centroid_average(centroid, features, num_features):
    centroid_average = [0] * num_features
    for i in range(num_features):
        for user in centroid.closests:
            centroid_average[i] = centroid_average[i] + features[user][i]
        return [centroid_dimension / len(centroid.closests) for centroid_dimension in centroid_average]