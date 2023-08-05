def load_barbell(weight):
    anslist = [] 
    weights = [25, 20, 15, 10, 5, 2.5, 2, 1.5 , 1, 0.5, "c"]
    letters = ["R", "B", "Y", "G", "W", "r", "b", "y", "g", "w", "c"]
    weight = weight/2-12.5
    x = 0
    while x != 10 and weight != 0:
        if weight >= weights[x]:
            weight -= weights[x]
            anslist.append(weights[x])
        else: x += 1
    anslist.insert( next((i for i, num in enumerate(anslist) if num < 2.4), len(anslist)), "c")
    return [letters[weights.index(x)] for x in anslist]

def adjust_barbell(weight_start, weight_end):
    ans = []
    weight_start = load_barbell(weight_start)
    weight_end = load_barbell(weight_end)
    index = len(weight_start)
    try:
        for i in range(len(weight_start)):
            if weight_start[i] != weight_end[i]:
                index = i
                break
        for j in range(len(weight_start)-1,index-1, -1): ans.append(f"strip {weight_start[j]}")
        for x in range(index, len(weight_end)):ans.append(f"load {weight_end[x]}")
    except: 
        for num in range(len(weight_start)):
            if len(weight_end) == num or weight_start[num] != weight_end[num]: index = num
        for item in range(len(weight_start)-1,index-1,-1): 
            ans.append(f"strip {weight_start[item]}")
    return ", ".join(ans) 
print(adjust_barbell(48, 45)) 