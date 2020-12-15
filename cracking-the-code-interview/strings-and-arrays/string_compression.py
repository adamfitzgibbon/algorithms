"""Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string 'aabccccaaa' would become 'a2b1c4a3'. If the "compressed" string would not become smaller than the orginal string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a-z)"""

def string_compression(s):
    char = s[0]
    count = 0
    comp = []
    for c in s:
        if c == char:
            count += 1
        else:
            comp.append(char + str(count))
            char = c
            count = 1
    comp.append(char + str(count))
    comp_str = "".join(comp)
    if len(comp_str) >= len(s):
        return s
    return comp_str

assert string_compression("aabccccaaa") == "a2b1c4a3"
assert string_compression("abc") == "abc"