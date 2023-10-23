def scoreboard(s):
    ans = []
    nums = ["nil", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for num in nums:
        for _ in range(2):
            if num in s:
                ans.append([s.index(num),nums.index(num)])
                s = s[:s.index(num)] + s[s.index(num) +  2:]
    ans.sort()
    return [ans[0][1], ans[1][1]]