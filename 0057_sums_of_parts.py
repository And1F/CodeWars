def parts_sums(ls):
    ans = [sum(ls)]
    for i in range(len(ls)):
        ans.append(ans[-1]-ls[i])
    return(ans)
print(parts_sums([1,2,3,4,5,6]))