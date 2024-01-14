def prime_factors_count(n):
    count = 0
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            count += 1
    if n > 1:
        count += 1
    return count

def kprimes_step(k, step, start, nd):
    result = []
    
    for num in range(start, nd + 1):
        if prime_factors_count(num) == k:
            result.append(num)
    
    pairs = []
    for i in range(len(result) - 1):
        j = 0
        while result[j]<= result[i]+step and i+j < len(result):
            if result[i + j] - result[i] == step:
                pairs.append([result[i], result[i + j]])
            j +=1
    return pairs