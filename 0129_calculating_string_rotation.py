def shifted_diff(first, second):
    for i in range(len(second)):
        print(first)
        if first == second: return i
        else: 
            second = second[1:] + second[0]
    return -1