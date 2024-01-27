def travel_chessboard(s):
    x1, y1, x2, y2 = int(s[1]), int(s[3]), int(s[6]), int(s[8]),

    grid = [[0] * (y2 - y1 + 1) for _ in range(x2 - x1 + 1)]
    grid[0][0] = 1

    for i in range(1, x2 - x1 + 1):
        grid[i][0] = grid[i - 1][0]

    for i in range(1, y2 - y1 + 1):
        grid[0][i] = grid[0][i - 1]

    for i in range(1, x2 - x1 + 1):
        for j in range(1, y2 - y1 + 1):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    return grid[-1][-1]