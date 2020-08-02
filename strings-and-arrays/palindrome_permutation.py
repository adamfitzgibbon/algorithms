"""Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards. 
A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words. 
You can ignore casing and non-letter characters."""

def palindrome_permutation(s):
    s = s.replace(" ", "").lower()
    dict = {}
    for char in s:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    oneCount = 0
    for item in dict.values():
        if item == 1:
            oneCount += 1
        elif item % 2 != 0:
            return False
    return (len(s) % 2 == 0 and oneCount == 0) or oneCount == 1

assert palindrome_permutation("Tact Coa")
assert palindrome_permutation("aaaabbbbcccc")
assert not palindrome_permutation("abc")