def camel_case(s):
    return "".join([x[0].upper() + x[1:].lower() for x in s.split(" ")if x != ""])


print(camel_case("say hello "))