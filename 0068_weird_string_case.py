def to_weird_case(words):
    words = words.split(" ")
    ans = []
    for word in words:
        ans.append("".join([word[i].upper() if i%2 == 0 else word[i].lower() for i in range(len(word))]))
    return " ".join(ans)
print(to_weird_case("ab ab ab"))