def josephus(items,k):
    rtr = []
    rest = k
    for _ in range(len(items)):
        ln = len(items)
        move = items[rest]
        rtr.append(move)
        del move
        rest = k - (ln - 1 - (rest-1)%ln)

    return rtr


print(josephus(["C","o","d","e","W","a","r","s"],4))