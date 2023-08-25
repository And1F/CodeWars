def solution(args):
    index = 0
    start = 0
    while True:
        if index == len(args)-2:
            if index != start: 
                if args[index] +1 == args[index +1]: index += 1
                if start+1 != index:
                    args.insert(start, f"{args[start]}-{args[index]}")
                    del args[start+1:index+2]
            break

        if args[index] +1 == args[index +1]:            
            index += 1
        else: 
            if index != start and start+1 != index:
                args.insert(start, f"{args[start]}-{args[index]}")
                del args[start+1:index+2]
            index = start + 1
            start += 1

    return ",".join([str(item) for item in args])

a = [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,18,19,20]
b = [-3,-2,-1,0,1,3]
print(solution(a))
