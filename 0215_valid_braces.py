def valid_braces(string):
    lst = []
    map = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in map.values():
            lst.append(char)
        elif char in map:
            if not lst or lst.pop() != map[char]: return False
        else: return False

    return not lst