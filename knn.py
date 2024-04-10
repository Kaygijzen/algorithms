import math


def euclidean_distance(a, b):
    assert len(a) == len(b)
    return math.sqrt(sum([(a[j] - b[j]) ** 2 for j in range(len(a))]))
    

def k_nearest_neighbour(x, X, k):
    distances = []
    for i, X_i in X.items():
        for item in X_i:
            distance = euclidean_distance(x, item)

            distances.append((distance, i))

    distances.sort(key=lambda x: x[0])

    counts = { c: 0 for c in X.keys() }

    for i in range(k):
        j = distances[i][1]
        counts[j] += 1

    return max(counts, key=counts.get)
    

if __name__ == '__main__':
    X = {
        0:[(1,12),(2,5),(3,6),(3,10),(3.5,8),(2,11),(2,9),(1,7)],
        1:[(5,3),(3,2),(1.5,9),(7,2),(6,1),(3.8,1),(5.6,4),(4,2),(2,5)]
    }
    p = (2.5,7)
    k = 3
    
    nn = k_nearest_neighbour(p, X, k)
    
    print("point", p, "is classified as class:", nn)