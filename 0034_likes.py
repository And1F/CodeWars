def likes(names):
    number_of_likes = len(names)
    if number_of_likes == 0: return "no one likes this"
    elif number_of_likes == 1: return f"{names[0]} likes this"
    elif number_of_likes == 2: return f"{names[0]} and {names[1]} likes this"
    elif number_of_likes == 3: return f"{names[0]}, {names[1]} and {names[2]} likes this"
    else: return f"{names[0]} and {names[1]} and {number_of_likes-2} others likes this"
print(likes(["Alex", "Jacob", "Mark", "Max"]))