def delete_nth(order:list,max_e:int)->list:
    ans = []
    for i in order:
        if ans.count(i) < max_e: ans.append(i)
    return ans