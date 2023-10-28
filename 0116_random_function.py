def strong_enough(earthquake, age):
    building_hp = pow(0.99,age)*1000
    earthquake = [x[0]+x[1]+x[2] for x in earthquake]
    earthquake_strength = earthquake[0]*earthquake[1]*earthquake[2]
    if earthquake_strength > building_hp: return "Needs Reinforcement!"
    else: return "Safe!"