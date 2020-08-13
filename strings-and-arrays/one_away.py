"""There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. 
Given two strings, write a function to check if they are one edit (or zero edits) away."""

def one_away(s1, s2):
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)
    return False

def one_edit_replace(s1, s2):
    found = False
    for i, char in enumerate(s1):
        if char != s2[i]:
            if (found):
                return False
            found = True
    return True

def one_edit_insert(s1, s2):
    s1i = 0
    s2i = 0
    while s1i < len(s1) and s2i < len(s2):
        if s1[s1i] != s2[s2i]:
            if s1i != s2i:
                return False
            s2i += 1
        else:
            s1i += 1
            s2i += 1
    return True

assert one_away("pale", "ple")
assert one_away("pales", "pale")
assert one_away("pale", "bale")
assert not one_away("pale", "bake")