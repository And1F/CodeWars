def nb_dig(n, d):
    ans = 0
    for num in range(n+1):
        if str(d) in str(num**2): 
            ans += str(num**2).count(str(d))
    return ans

print(nb_dig(10,1))