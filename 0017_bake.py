def bake(recipe, available):
    a = []
    try:
        for ingredient in list(recipe.keys()):
            a.append(available[ingredient]/recipe[ingredient])
        return int(min(a)//1)
    except:
        return 0
