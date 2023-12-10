def scf (arr):
    if arr == []: return 1
    for scf in range(2,min(arr)+1):
        ans = True
        for num in arr:
            if num % scf != 0: ans = False
        if ans:return scf
    return 1