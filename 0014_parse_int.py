def parse_int(string):
    print(string)
    if string == "zero":
        return 0
    string = string + " "
    num1_90 = ["one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", " and", "0-"]
    num90 = ["1 ","2 ","3 ","4 ","5 ","6 ","7 ","8" ,"9 ","10", "11", "12", "13", "14", "15", "16", "17", "18", "19","20","30","40","50","60","70","80","90", "", ""]
    rest_num = ["hundred", "thousand", "million"]
    for word in num1_90:
        string = string.replace(word, num90[num1_90.index(word)])
    print(string)
    lst = string.split()
    num = 0
    while num != len(lst):
        if lst[num] == "hundred":
            if len(lst)-1> num and lst[num+1].isnumeric():
                lst[num-1] = f"{lst[num-1]}{lst[num+1]}" if int(lst[num+1]) > 9 else f"{lst[num-1]}0{lst[num+1]}"
                del lst[num+1]
            else: lst[num-1] = f"{lst[num-1]}00"
            del lst[num]
        elif lst[num] == "thousand":
            lst[num-1] = f"{lst[num-1]}000"
            del lst[num]
        else: num +=1
    return sum([int(x) for x in lst])

print(parse_int("eight hundred eighty-eight thousand eight hundred and eighty-eight"))#783_919