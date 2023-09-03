def expanded_form(num):
    return " + ".join([str(num)[x] + "0"*(len(str(num))-x-1) for x in range(len(str(num))) if str(num)[x] != "0"])


print(expanded_form(10234))