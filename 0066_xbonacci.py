def Xbonacci(signature,n):
    ln = len(signature)
    ans = signature[:n]
    while len(ans) != n:
        add = sum(ans[-ln:])
        ans.append(add)
    return ans
print(Xbonacci([0,0,0,0,1],10))