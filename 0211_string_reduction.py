def solve(a, b):
    if all(a.count(char) >= b.count(char) for char in set(b)):
        return sum(max(0, a.count(char) - b.count(char)) for char in set(a))
    else:
        return 0  