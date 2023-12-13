def cycle(n):
    if n % 2 == 0 or n % 5 == 0: return -1
    all_rest = {}
    rest = 1
    position = 0

    while rest != 0:
        if rest in all_rest:
            return position - all_rest[rest]
        all_rest[rest] = position
        rest = (rest * 10) % n
        position += 1
    
    return -1