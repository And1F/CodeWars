def last_digit(lst):
    print(lst)
    if not lst: return 1
    elif len(lst) == 1: return int(str(lst[0])[-1])
    elif len(lst) == 2: return pow(lst[0], lst[1], 10)
    else: 
        for i in range(len(lst)-1, 1,-1):
            lst[i-1] = pow(lst[i-1], lst[i],100000000000000000000000000000000000000)
        return pow(lst[0], lst[1], 10)
    
print(last_digit([12, 30, 21]))
  