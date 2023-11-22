def make_password(phrase):
    replacements = {'i': '1', 'I': '1', 'o': '0', 'O': '0', 's': '5', 'S': '5'}
    return ''.join(replacements.get(word[0], word[0]) for word in phrase.split())