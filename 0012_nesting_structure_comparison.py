def same_structure_as(a,b):
    print(a,b)
    if isinstance(a, list) and isinstance(b, list):
        for lst in [a,b]:
           nullifier(lst)
        return a==b
    else:
        return False

def nullifier(lst):
    for num in range(len(lst)):
        if not isinstance(lst[num], list):
            lst[num] = 0
        else:
            nullifier(lst[num])

print(same_structure_as([1,[1,1]],1))
