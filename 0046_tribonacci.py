def tribonacci(signature, n):
    for i in range(n-3):
        signature.append(signature[-1]+signature[-2]+signature[-3])
    return signature[:n]
print(tribonacci([0, 1, 1], 10))