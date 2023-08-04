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
    anslist = "".join([letters[weights.index(x)] for x in anslist])
    return "-"*(10-len(anslist)) + anslist[::-1] + "-"*20 + anslist + "-"*(10-len(anslist))
print(load_barbell(35))