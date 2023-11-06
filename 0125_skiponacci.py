def skiponacci(n):
    ans = "1"
    a = 1
    b = 1
    for i in range(n-1):
        b = a + b
        a = b - a
        if i % 2 == 0: ans += " skip"
        else: ans += f" {a}"
    return ans