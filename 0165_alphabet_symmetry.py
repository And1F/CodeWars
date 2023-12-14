def solve(strings : list[str]) -> list[int]:
    ans = []
    for string in strings:
        count = 0
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(min(len(string),len(alphabet))):
            if alphabet[i] == string.lower()[i]:
                count += 1
        ans.append(count)
    return ans