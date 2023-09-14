s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"

def meeting(string):
    stringlist = [[y.upper() for y in x.split(":")] for x in string.split(";")]
    stringlist = sorted([(x[1],x[0]) for x in stringlist]).
    ans = ""
    for i in stringlist:
        ans += str(i).replace("'","")
    return ans
print(meeting(s))
