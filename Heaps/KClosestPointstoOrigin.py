import heapq


def k_closest_points(points, k):
    minHeap = []

    for x,y in points:
        dist = x**2 + y**2
        minHeap.append([dist,x,y])
    heapq.heapify(minHeap)

    res = []
    while k > 0:
        dis,x,y = heapq.heappop(minHeap)
        res.append([x,y])

        k -=1

    return  res




if __name__ == '__main__':
    points = [[1, 3], [-2, 2]]
    k = 1
    val = k_closest_points(points, k)
    print(val)