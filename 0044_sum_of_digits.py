def digital_root(n):
    ans = 0
    for char in str(n):
        ans += int(char)
    while len(str(ans)) > 1:
        ans = digital_root(ans)
    return ans

digital_root(1456)