def barbell_weight(barbell):
    weights = {"R":25, "B":20, "Y":15, "G":10, "W":5, "r":2.5, "c":2.5, "b":2, "y":1.5, "g":1, "w":0.5, "-":0}
    ans = sum([weights[wheight] for wheight in barbell])+20
    return int(ans) if ans%1 == 0 else ans


print(barbell_weight("-----bcrBR--------------------RBrcb-----"))