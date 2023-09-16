def encode(st):
    vowels = {"a":"1","e":"2","i":"3","o":"4","u":"5"}
    for k in vowels.keys():
        st = st.replace(k,vowels[k])
    return st
    
def decode(st):
    vowels = {"a":"1","e":"2","i":"3","o":"4","u":"5"}
    for k in vowels.keys():
        st = st.replace(vowels[k],k)
    return st

print(encode('hello'))