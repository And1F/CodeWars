def longest_palindrome(s):
    length = 0
    odd = False
    
    count = {}
    for char in s.lower():
        if char.isalnum():
            count[char] = count.get(char, 0)+1

    for e in count.values():
        if e % 2 == 0:
            length += e
        else:
            length += e - 1
            odd = True
            
    return length+1 if odd else length

