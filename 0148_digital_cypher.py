def encode(m, k):
    return [ord(m[i])-96 + [int(x) for x in str(k)][i%len(str(k))]for i in range(len(m))]