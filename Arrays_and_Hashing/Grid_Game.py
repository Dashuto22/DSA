def grid_game(grid):
    cols = len(grid[0])
    prefixr1, prefixr2 = grid[0].copy(), grid[1].copy()

    for i in range(1, cols):
        prefixr1[i]+=prefixr1[i-1]
        prefixr2[i]+=prefixr2[i-1]

    res = float("inf")

    for i in range(cols):
        top =  prefixr1[-1]-prefixr1[i]
        bottom = prefixr2[i-1] if i>0 else 0

        secondrobo = max(top, bottom)
        res = min(res, secondrobo)

    return res



if __name__ == '__main__':
    grid = [[2, 5, 4], [1, 5, 1]]
    val = grid_game(grid)
    print(val)