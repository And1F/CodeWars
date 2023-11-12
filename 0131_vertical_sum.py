def vertical_sum(n, i):
    n = n-1
    i += n
    ans = 0
    for k in range(n+1):
        if k+i < n or i-k>n: 
            pass
        else:
            bottom_left = sum([x for x in range(1,k+1)])
            if n%2 ==0:
                ans += bottom_left+1+(i-n+k)/2 if (i%2 == 0 and k%2 ==0) or (i%2 == 1 and k%2 ==1) else 0
            else:
                ans += bottom_left+1+(i-n+k)/2 if not((i%2 == 0 and k%2 ==0) or (i%2 == 1 and k%2 ==1)) else 0
    return ans