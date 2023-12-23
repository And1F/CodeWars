def directions(goal):
    ans = []
    dir = [goal.count("N") - goal.count("S"), goal.count("E") - goal.count("W")]

    if dir[0] > 0: ans += ["N" for _ in range(dir[0])]
    elif dir[0] < 0: ans += ["S" for _ in range(abs(dir[0]))]

    if dir[1] > 0: ans += ["E" for _ in range(dir[1])]
    elif dir[1] < 0: ans += ["W" for _ in range(abs(dir[1]))]

    return ans