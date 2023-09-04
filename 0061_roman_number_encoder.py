def solution(roman):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    ans = 0
    pre = 0
    for char in reversed(roman):
        value = roman_dict[char]
        if value < pre:ans -= value
        else: ans += value
        pre = value
    return ans

print(solution('MMVIII'))