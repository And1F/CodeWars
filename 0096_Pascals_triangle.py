def pascals_triangle(n):
    ans  = [1]
    for row in range(1,n):
        ans.append(1)
        for num in range(1,row):
            ans.append(last_row[num]+last_row[num-1])
        ans.append(1)
        last_row = ans[-row-1:]
    return ans


print(pascals_triangle(1000))
