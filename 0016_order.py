def order(sentence):
    a = sentence.split(" ")
    b=[0 for x in range(len(a))]
    for i in a:
        b.insert([int(num) for num in i if num.isdigit()][0],i)
        try:
            del b[[int(num) for num in i if num.isdigit()][0]+1]
        except:
            pass
    del b[0]
    return " ".join(b)


print(order("is2 Thi1s T4est 3a"))