def strip_comments(strng, markers):
    copy = True
    ans = ""
    num = 0
    while num != len(strng):
        if strng[num] in markers:
            copy = False
        elif strng[num] == "\n":
            copy = True
        if copy:
            ans  = ans + strng[num]
        num +=1
    return "\n".join(line.rstrip() for line in ans.split("\n"))

print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))