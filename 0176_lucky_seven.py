import math

def lucky_sevens(arr):
    count = 0
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] == 7:
                _sum = 0
                if y - 1 >= 0: _sum += arr[y - 1][x]
                if y + 1 < len(arr): _sum += arr[y + 1][x]
                if x - 1 >= 0: _sum += arr[y][x - 1]
                if x + 1 < len(arr[y]): _sum += arr[y][x + 1]
                if int(math.pow(_sum, 1/3)-0.001)+1 == int(math.pow(_sum, 1/3)+0.000005):
                    count += 1
    return count