def search_perm_mult(n_max, k):
    ans = 0
    for i in range(1,int(n_max/k)+1):
        if sorted([x for x in str(i)]) == sorted([x for x in str(i*k)]):
            ans += 1
    return ans