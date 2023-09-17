def highest_rank(arr):
    ans = []
    for num in set(arr):
        ans.append([arr.count(num),num])
    return sorted(ans)[-1][-1]
