import math
def is_prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

def not_primes(a, b):
    ans = []
    for num in range(a,b):
        if [x for x in str(num) if x in ["1","4","6","8","9","0"] ] == [] and not is_prime(num):
            ans.append(num)
    return ans