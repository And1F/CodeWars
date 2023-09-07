def solution(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    ans = ''
    i = 0

    while num > 0:
        for _ in range(num // val[i]):
            ans += syms[i]
            num -= val[i]
        i += 1
    return ans