from math import sqrt
def sum_of_squares(n):
    ans = []
    a = n
    for i in range(0,int(sqrt(sqrt(n)))):
        num = 0
        n = a
        n -= (int(sqrt(n))-i)**2
        num +=1
        while n != 0:
            n -= int(sqrt(n))**2
            num +=1
        ans.append(num)
    return min(ans)


print(sum_of_squares(16))
 