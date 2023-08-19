def highest_word(string):
    words = string.split()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    score = []
    for word in words:
        ans = 0
        for char in word:
            ans += alphabet.index(char)+1
        score.append(ans)
    return words[score.index(max(score))]
print(highest_word('what time are we climbing up the volcano'))