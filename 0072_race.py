def race(v1, v2, g):
    if v1>=v2: return None
    t = round(g/(-v1 + v2),10) 
    ans = [round(t//1)]
    for _ in range(2):
        t = (t-int(t))*60
        ans.append(round(t))
    return ans
print(race(80, 91, 37))