def is_valid_IP(strng):
    if strng.count(".") != 3: return False
    elif len([0 for x in strng if x.isdigit() or x == "."]) != len(strng): return False
    elif len([x for x in strng.split(".") if x == "" 
              or int(x) > 255 or (x[0] == "0" and x != "0")]) > 0: return False
    return True
print(is_valid_IP('12.255.56.1'))