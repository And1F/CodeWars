def is_pangram(s):
    for char in "abcdefghijklmnopqrstuvwxyz":
        if not char in s.lower():
            return False
    return True