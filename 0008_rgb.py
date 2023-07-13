def rgb(r, g, b):
    ans = ""
    for num in (r,g,b):
        if num > 255:
            add = hex(255)[2:].upper()
        elif num < 0:
            add = "0" + hex(0)[2:].upper()
        elif num < 16:
            add = "0" + hex(num)[2:].upper()
        else:
            add = hex(num)[2:].upper()
        ans = ans + add
    return ans


print(rgb(0X141137D))
print(hex(249)[2:].upper())
