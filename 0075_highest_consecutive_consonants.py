def solve(string):
    cnt = 0
    ans = []
    for letter in string:
        if letter not in ["a", "e", "i", "o", "u"]:
            cnt += "abcdefghijklmnopqrstuvwxyz".index(letter) + 1
        else:
            ans.append(cnt)
            cnt = 0
    ans.append(cnt)
    return max(ans)