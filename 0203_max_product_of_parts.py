def maximum_product_of_parts(n):
    return max(int(str(n)[:i]) * int(str(n)[i:j]) * int(str(n)[j:]) for i in range(1, len(str(n)) - 1) for j in range(i + 1, len(str(n))))
