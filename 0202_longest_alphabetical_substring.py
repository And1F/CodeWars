def longest(s):
    max = s[0]
    current = s[0]

    for i in range(1, len(s)):
        if ord(s[i]) >= ord(s[i-1]):
            current += s[i]
        else:
            current = s[i]

        if len(current) > len(max):
            max = current

    return max