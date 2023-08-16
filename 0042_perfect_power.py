import math
def isPP(n):
    for num in range(2, int(math.sqrt(n))+1):
        print(math.log(n,num))
        if round(math.log(n,num),10) % 1 == 0:
            return [num, round(math.log(n,num))]
    return None                
print(isPP(380204032))
print(52**5)