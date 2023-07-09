def first_non_repeating_letter(string):
    for letter in string:
        print(letter, string.upper().count(letter.upper()))
        if string.upper().count(letter.upper()) == 1:
            return letter
    return ""
print(first_non_repeating_letter('hello world, eh?'))