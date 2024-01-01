def largest_sum(arr):
    if arr == []: return 0
    mx = 0
    sum = 0

    for num in arr:
        sum = max(0, sum + num)
        mx = max(mx, sum)

    return mx