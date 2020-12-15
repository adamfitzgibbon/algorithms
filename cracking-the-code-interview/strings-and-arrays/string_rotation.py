"""Assume you have a method isSubstring which checks if one words is a substring of another. 
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g. "waterbottle" is a rotation of "erbottlewat")"""

# TODO: come back and actually use isSubstring in the solution (misunderstood the question on the first attempt)
def string_rotation(s1, s2):
    for i in range(len(s1)):
        if s2 == s1[len(s1)-i - 1:] + s1[: len(s1)-i -1]:
            return True
    return False

assert string_rotation("waterbottle", "erbottlewat")