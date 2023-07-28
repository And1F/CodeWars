def generate_hashtag(s):
    if s == "" or len(s) > 140:
        return False
    return "#"+"".join([x[:1].upper()+(x[1:]).lower() for x in s.split()])

    

print(generate_hashtag('CoDeWaRs is niCe'))