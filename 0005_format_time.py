def format_duration(seconds):
    times = {"year":31536000, "day":86400, "hour":3600,  "minute":60, "second":1}
    string = []
    if seconds < 1:
        return "now"
    for time in times.items():
        minus = seconds//time[1]
        seconds -= minus*time[1]
        if minus == 1:
            string.append(f"{minus} {time[0]}")
        elif minus > 1:
            string.append(f"{minus} {time[0]}s")
    return " and".join(", ".join(string).rsplit(",", 1))

print(format_duration(33243586))  
