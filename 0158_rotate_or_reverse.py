def rev_rot(str, sz):
    ans = ""
    if len(str) < sz or sz == 0: return ans
    str = str[:(len(str)//sz)*sz]
    str = [str[x:x+sz] for x in range(0,len(str),sz)]
    for s in str:
        if sum([int(x) for x in s])%2 == 0:
            ans += s[::-1]
        else: ans += s[1:] + s[0]
    return ans