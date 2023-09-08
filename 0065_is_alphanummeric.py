def alphanumeric(password):
    if [x for x in password if x.isnumeric() or x.isalpha()] != list(password): return False
    elif password == "": return False
    return True