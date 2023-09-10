def up_array(arr):
    if "".join([str(x) for x in arr]).isnumeric() and [int(str(x)[0]) for x in arr] ==arr:
            if arr[0] ==0:
                if arr[1:] == [9 for x in range(len(arr)-1)]: pass
                else: 
                    ans = []
                    num  = int("".join([str(x) for x in arr])) + 1
                    while arr[0] == 0:
                        ans.append(0)
                        del arr[0]
                    return ans + [int(x) for x in list(str(num))]
            num = int("".join([str(x) for x in arr])) + 1
            print("a")
            return [int(x) for x in list(str(num))]
    return None

print(up_array([0,2,3,9]))
