def convert(s):
    hours = s // 3600
    minutes = (s % 3600) // 60
    seconds = s % 60
    return "{:02d}|{:02d}|{:02d}".format(int(hours), int(minutes), int(seconds))

def stat(strg):
    if strg == "": return ""
    stats = strg.split(", ")
    stats = [x.split("|") for x in stats]
    stats = sorted([int(x[0])*3600 + int(x[1])*60 + int(x[2]) for x in stats])
    range = max(stats)-min(stats)
    average = sum(stats)/len(stats)
    median = stats[int(len(stats)/2)] if len(stats)%2 == 1 else (stats[int(len(stats)/2)-1] + stats[int(len(stats)/2)])/2
    return f"Range: {convert(range)} Average: {convert(average)} Median: {convert(median)}"