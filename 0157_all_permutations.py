def recursion(base,left_overs,list):
    if left_overs == "": list.append(base)
    else:
        for i in range(len(left_overs)):
            recursion(base + left_overs[i],left_overs[:i] + left_overs[i+1:],list)


def permutations(s):
    result = []
    recursion("",s,result)
    return set(result)