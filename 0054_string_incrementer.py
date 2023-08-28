def increment_string(strng):
    if strng == "":return "1"
    elif not strng[-1].isdigit(): return strng + "1"
    elif strng[-1] != "9": return strng[:-1] + str(int(strng[-1])+1)
    elif strng[-1] == "9":
        if strng[-2] == "9":
            index = []
            for i in range(len(strng)-1,-1,-1):
                if strng[i] == strng[i-1] == "9":index.append(i-1)
                else:break
            index = index[-1]
            if strng[index-1].isdigit():return strng[:index-1] + str(int(strng[index-1:])+1)
            else: return strng[:index] + str(int(strng[index:])+1)
        elif strng[-2].isdigit(): return strng[:-2] + str(int(strng[-2])+1) + "0"
        else: return strng[:-1] + "10"
print(increment_string("foobar099"))
                       #0123456789

#String = 'e8MCSF+35068o9@[R)L412300365q0726791_bp|oq7090T866,Ia99512854p~003X*EF+900000009960965699': 
#         'e8MCSF+35068o9@[R)L412300365q0726791_bp|oq7090T866,Ia99512854p~003X*EF+9000000 9960965700' should equal 
#         'e8MCSF+35068o9@[R)L412300365q0726791_bp|oq7090T866,Ia99512854p~003X*EF+900000009960965700'