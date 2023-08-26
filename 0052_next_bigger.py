def next_bigger(num):
    if sorted(str(num), reverse=True) == [x for x in str(num)]:return -1
    num = str(num)
    indx = [x for x in range(len(num)-1) if num[x]<num[x+1]][-1] # find last index that is lower than successor
    before = num[:indx]
    after = sorted(num[indx:])
    first_higher = [after[x] for x in range(len(after)) if after[x] > num[indx]][0]
    after.pop(after.index(first_higher))
    return int(before +first_higher +"".join(after))
print(next_bigger(59884848459853))
#n=59884848459853: 
#  59884848493558 should equal 
#  59884848483559