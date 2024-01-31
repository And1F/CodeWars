def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(*args):
    if not args: return 1
    if 0 in args: return 0

    result = args[0]
    for num in args[1:]:
        result = (result * num) // gcd(result, num)

    return result