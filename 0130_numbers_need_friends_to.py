def numbers_need_friends_too(n):
    if n < 10: return n * 111
    n = str(n)
    ans = n[0]
    if n[0] != n[1]: ans += 2*n[0]
    for i in range(1,len(n)-1):
        if n[i-1] != n[i] != n[i+1]: ans += 3*n[i]
        else: ans += n[i]
    if n[-1] != n[-2]: ans += 2*n[-1]
    return int(ans + n[-1])