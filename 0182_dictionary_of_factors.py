def factors_range(n, m):
    ans = dict([x,[y for y in range(2,x) if x%y==0 and y!=1]] for x in range(n,m+1))
    for i in range(n,m+1):
        if ans[i] == []:
            ans[i] = ['None']
    return ans