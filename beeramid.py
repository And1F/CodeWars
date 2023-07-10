def beeramid(money, beerprice):
    if money < 1:
        return 0
    beer = money/beerprice
    for num in range(money):
        beer -= num ** 2
        if beer < (num+1) ** 2:
            return num

print(beeramid(1500, 2))