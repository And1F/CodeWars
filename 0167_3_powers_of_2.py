from math import log
def three_powers(n):
    if bin(int(n/3))[2:].count('1') == 1: 
        return True
    for e in range(int(n/2)+1):
        if 2**e > n: break
        num  = int((n-2**e)/2) if (n-2**e) % 2 == 0 else 0
        if bin(int(num))[2:].count('1') == 1 and 2*num + 2**e == n:
            return True 
    return bin(n)[2:].count('1') == 3


print(three_powers(158456325028816909965581090816))
