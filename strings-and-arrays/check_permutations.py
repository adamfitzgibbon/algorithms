"""Given two strings, write a method to decide if one is a permutation of the other."""

def isPerm(s1, s2):
    return sorted(s1) == sorted(s2)

assert isPerm("abc", "bac")
assert isPerm("foo bar", "brfo ao")

# TODO: Come back to this and implement the O(n) solution