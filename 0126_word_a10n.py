import re
def replace_word(match):
    word = match.group(0)
    if len(word) >= 4:
        return word[0] + str(len(word) - 2) + word[-1]
    else:
        return word
def abbreviate(s):
    ans = re.sub(r'[A-Za-z]+', replace_word, s)
    return ans