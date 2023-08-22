def wave(people):
    return [people[:x] + people[x].upper() + people[x+1:] for x in range(len(people))]

print(wave("hello"))