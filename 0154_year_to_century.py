def what_century(year):
    year = str(int(year)+99)[:-2]
    if year[-1] == "1" and year[0] != "1": return year + "st"
    elif year[-1] == "2" and year[0] != "1": return year + "nd"
    elif year[-1] == "3" and year[0] != "1": return year + "rd"
    else: return year + "th"

