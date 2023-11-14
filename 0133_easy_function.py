def one_two_three(n):
    if n == 0: return [0,0]
    ans = n//9*"9"
    if n%9 != 0: ans += f"{n%9}"
    return [int(ans),int("1"*n)]
    