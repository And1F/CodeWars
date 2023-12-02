def diagonal(m):
    ans = []
    for i in range(len(m)):
        for j in range(i+1):
            ans.append(m[len(m)-1-i+j][len(m)-1-j])
            
    for i in range(len(m)-1):
        for j in range(len(m)-i-1):
            print(j,i)
            ans.append(m[j][len(m)-2-j-i])
    return ans

    