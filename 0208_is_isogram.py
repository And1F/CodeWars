def is_isogram(s):
    chars = set()

    for c in s.lower():
        if c.isalpha():
            if c in chars:
                return False
            chars.add(c)

    return True