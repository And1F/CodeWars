def binary_array_to_number(arr):
    multiplikator = 1
    ans = 0
    for i in range(len(arr)-1,-1,-1):
        ans += arr[i]*multiplikator
        multiplikator *= 2
    return ans