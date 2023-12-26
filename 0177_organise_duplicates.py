def group(arr):
    ans = []
    for i in range(len(arr)):
        if arr.index(arr[i]) == i:
            ans.append([arr[i]]*arr.count(arr[i]))
    return ans