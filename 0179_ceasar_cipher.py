def one_down(txt):
    ans = ""
    if type(txt) != str: return "Input is not a string"
    for char in range(len(txt)):
        if not txt[char].isalpha(): ans += txt[char]
        elif txt[char] == "A": ans += "Z"        
        elif txt[char] == "a": ans += "z"
        else: ans += chr(ord(txt[char]) - 1)
    return ans