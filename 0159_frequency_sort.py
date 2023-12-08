def most_common(arr):
    num = arr[0]
    for i in arr:
        if arr.count(i)>arr.count(num):
            num = i
        elif arr.count(i) == arr.count(num) and num>i:
            num = i
    return [num,arr.count(num)]

def recursion(arr,ans):
    if arr == []: pass
    else: 
        lst = most_common(arr)
        print(lst)
        ans.extend([lst[0] for _ in range(lst[1])])
        arr = [x for x in arr if x != lst[0]]
        recursion(arr,ans)
        

def solve(arr):
    ans = []
    recursion(arr,ans)
    return ans
    