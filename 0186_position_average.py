def pos_average(s):
    s = s.split(", ")
    common = 0
    total = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            for k in range(len(s[i])):
                if s[i][k] == s[j][k]: common += 1
                total += 1
    return common/total*100