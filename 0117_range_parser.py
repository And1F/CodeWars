def range_parser(string):
    ans = []
    string = string.split(",")
    for s in string:
        if ":" in s:
            for num in range(int(s[:s.index("-")]), 
                             int(s[s.index("-")+1:s.index(":")])+1, 
                             int(s[s.index(":")+1:])):
            
                ans.append(num) 
        elif "-" in s:
            for num in range(int(s[:s.index("-")]), int(s[s.index("-") + 1:])+1):
                ans.append(num)
        else: ans.append(int(s))
    return ans
print(range_parser('1-10,14, 20-25:2'))