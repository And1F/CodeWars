def find_missing_letter(chars):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(alphabet.index(chars[0].lower()),len(chars)+alphabet.index(chars[0].lower())):
        if alphabet[i] not in [x.lower() for x in chars]:
            return alphabet[i] if chars[0] in alphabet else alphabet[i].upper() 

a = find_missing_letter(['O','Q','R','S'])