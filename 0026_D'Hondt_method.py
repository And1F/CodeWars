def distribute_seats(num_seats: int, votes: tuple[int, ...])-> list[int]: 
    if num_seats == 0:
        return [0 for x in range(len(votes))]
    ans = [[votes[0]/x,0] for x in range(1,num_seats+1)]
    for num in range(1,len(votes)):
        challenger = [votes[num]/x for x in range(1,num_seats+1)]
        challenger.append(0)
        while min(ans)[0] < max(challenger):
            add = challenger.pop(challenger.index(max(challenger)))
            ans.append([add,num])
            ans = sorted(ans, reverse=True)
            if ans[-1][0] == ans[-2][0]:del ans[-2]
            else: del ans[-1]
    return [[x[1] for x in ans].count(x) for x in range(len(votes))]


numSeats = 4
votes = (1, 2, 3) 
expected = [4,2,1,1,0,0]
print(distribute_seats(numSeats,votes))

# 4 (1000, 2000, 340000)
# 4 (1, 2, 3) 