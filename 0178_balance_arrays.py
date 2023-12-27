def balance(arr1, arr2):
    return sorted([arr1.count(x) for x in arr1]) == sorted([arr2.count(x) for x in arr2])