def least_cuts(wall):
    gapMap = {0:0}

    for r in wall:
        total = 0
        for b in r[:-1]:
            total += b
            gapMap[total] = 1 +gapMap.get(total, 0)

    return len(wall) - max(gapMap.values())



if __name__ == '__main__':
    wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
    val = least_cuts(wall)
    print(val)