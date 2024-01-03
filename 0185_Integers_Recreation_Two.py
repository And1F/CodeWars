def prod2sum(a, b, c, d):
    n = (a**2 + b**2) * (c**2 + d**2)
    ans = []
    for e in [a*b+c*d,a*b-c*d,c*d-a*b,a*c+b*d,a*c-b*d,b*d-a*c,a*d+b*c,a*d-b*c,b*c-a*d]:
        if e < 0 or e**2>(a**2+b**2)*(c**2+d**2): continue
        f = ( (a**2+b**2)*(c**2+d**2) - e**2 )**(0.5)
        if int(f) == f and sorted([int(e),int(f)]) not in ans: ans.append(sorted([int(e),int(f)]))

    return sorted(ans)