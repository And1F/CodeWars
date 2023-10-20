def alphabet_war(fight):
    fight = [char for char in fight]
    left = 0
    right = 0
    for i in range(1,len(fight)-1):
        if fight[i] == "*":
            fight[i-1] = " "
            if fight[i+1] == "*": pass
            else: fight[i+1] = ""
    if fight[0] == "*": fight[1] = " "
    if fight[-1] == "*": fight[-2] = " "
    for char in fight:
        if char in ["s", "b", "p", "w"]: left += ["s", "b", "p", "w"].index(char) + 1
        elif char in ["z", "d", "q", "m"]: right += ["z", "d", "q", "m"].index(char) + 1
        print(right, left)
    if left > right: return "Left side wins!"
    elif left < right: return "Right side wins!"
    else: return "Let's fight again!"

print(alphabet_war("zdqmwpbs"))