def average_string(s):
    strings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", " "]
    if not s.split() or any(word not in strings for word in s.split()): return "n/a"
    nums = [[i, s.count(strings[i])] for i in range(10) if strings[i] in s]
    print(nums)
    c = 0
    ans = 0
    for i in nums:
        c += i[1]
        ans += i[1] * i[0]
    return "n/a" if nums == [] else strings[int(ans / c)]
