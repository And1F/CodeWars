def shortest_steps_to_num(num):
    steps = 0

    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        steps += 1
    return steps