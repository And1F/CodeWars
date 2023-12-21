def run_length_encoding(s):
    if s == "": return []
    ans = []
    i = 0
    c = 1
    j = 1
    while j != len(s):
        if s[j] != s[i]:
            ans.append([c,s[i]])
            i = j
            c = 1
        else:
            c += 1
        j += 1

    ans.append([c,s[i]])
    return ans