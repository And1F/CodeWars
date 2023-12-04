def duplicate_count(text):
    count = 0
    used = []
    for c in text.lower():
        if c not in used and text.lower().count(c)>1:
            used.append(c)
            count += 1
    return count