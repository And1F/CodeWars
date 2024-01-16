def solution(arr1, arr2):
    return sum((abs(x - y) ** 2) for x, y in zip(arr1, arr2)) / len(arr1)