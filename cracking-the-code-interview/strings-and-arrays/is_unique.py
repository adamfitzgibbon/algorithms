"""Check if a string is made up of all unique characters. Do it without another data structure."""

def isUnique(s):
    dict = {}
    for char in s:
        if char in dict:
            return False
        dict[char] = char
    return True

assert isUnique("abcde")
assert not isUnique("aabcd")
assert not isUnique("abbbbcd")

def isUniquesNoDS(s):
    for i, char in enumerate(s):
        if char in s[i+1:]:
            return False
    return True

assert isUnique("abcde")
assert not isUnique("aabcd")
assert not isUnique("abbbbcd")