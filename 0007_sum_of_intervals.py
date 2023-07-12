def sum_of_intervals(intervals):
    return length(get_rid_of_overlapping(sorted(listing(intervals))))
    

def length(intervals):
    ans = 0
    for interval in intervals:
        ans += interval[1] - interval[0]
    return ans

def listing(intervals):
    lst = []
    for interval in intervals:
        lst.append(list(interval))
    return lst

def get_rid_of_overlapping(intervals):
    print(intervals)
    i = 0
    while i != len(intervals)-1:
        if intervals[i][1] > intervals[i+1][0]:
            if intervals[i][1] > intervals[i+1][1]:
                del intervals[i+1]          
            else:
                intervals[i+1][0] = intervals[i][1]
        else:
            i+=1
    print(intervals)
    return intervals

print(sum_of_intervals([(269, 356), (54, 65), (-100, 377), (447, 497), (-32, 143), (290, 376), (144, 183), (423, 487), (266, 300), (444, 459), (294, 318), (-485, 450), (-254, -243), (112, 492), (247, 394), (215, 355)]))
print(sorted([(269, 356), (54, 65), (-100, 377), (447, 497), (-32, 143), (290, 376), (144, 183), (423, 487), (266, 300), (444, 459), (294, 318), (-485, 450), (-254, -243), (112, 492), (247, 394), (215, 355)]))