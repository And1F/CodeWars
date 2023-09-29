import re
def simplify(expr):
    lst = []
    number = 0
    for num in range(len(expr)):
        x = expr[num]
        if not any(char.isalpha() for char in x):
            number += int(x)
            del expr[num]
        else:
            main = re.findall(r"[a-zA-Z].*", x)[0] if re.findall(r"[a-zA-Z].*", x) != [] else ""
            lst.append(main)
    itr = 0
    while itr != len(lst):
        m = lst[itr]
        indx = [num for num in range(len(lst)) if lst[num] == m]
        if len(indx) >1:
            prefactor  = sum([int(re.findall(r"[^a-zA-Z]*", expr[int(x)])[0]) for x in indx ])
            prefactor = f"+{prefactor}" if prefactor >= 0 else f"-{prefactor}"
            expr = [x for x in expr if x != expr[int(indx[0])]]
            lst = [lst[x] for x in range(len(lst)) if x !=lst.index(m)]
            expr.append(f"{prefactor}{m}")
        itr +=1
    print(expr)
    expr.append(number)
    return expr


print(simplify(['+4x^4', '+2x^2', '+2x^2', '+1']))