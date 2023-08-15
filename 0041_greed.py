def score(dice):
    for num in [2,3,4,6]:
        if dice.count(num) >= 3: return num*100 + dice.count(5)*50 + dice.count(1)*100
    if dice.count(1) >= 3: return 1000 + dice.count(5)*50 + (dice.count(1)-3)*100
    elif dice.count(5) >= 3: return 500 + (dice.count(5)-3)*50 + dice.count(1)*100
    return dice.count(5)*50 + dice.count(1)*100
print(score([5, 1, 3, 4, 1]))