def pig_it(text):
    text = text.split(" ")
    for num in range(len(text)):
        if text[num].isalpha() == True:
            text[num] = text[num][1:] + text[num][0] + "ay"
    return " ".join(text)
print(pig_it("Hello World !"), "after return")