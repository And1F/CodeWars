def autocomplete(input, dictionary):
    input = "".join([x for x in input if x.isalpha()])
    len_input = len(input) 
    ans = []
    for i in dictionary:
        if input.lower() == i[:len_input].lower(): ans.append(i)
    if len(ans) >= 5: return ans[:5]
    return ans