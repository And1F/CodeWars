def find_digit(num, nth):
    return int(("0"*(abs(nth)-len(str(num))+1) + str(abs(num)))[-nth]) if nth >0 else -1