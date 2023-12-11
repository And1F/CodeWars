import re
def calc(a, b):
    return (a + b) + (a - b) + (a * b) + (a // b) if b != 0 else None
def evaluate(eq):
    lst = list(map(int, re.findall(r'-?\d+', eq))) 
    for _ in range(len(lst)-1):
        if lst[1] == 0:  
            return None
        lst[0] = calc(lst[0], lst[1])
        del lst[1]    
    return lst[0]
