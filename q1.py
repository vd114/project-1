"""
Question 1

Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.

"""

def question1(s, t):
    if (len(t)==0): return "Please input two strings"
    len_t = len(t)
    len_s = len(s)
    list_t = list(t)
    list_t.sort()     # Quick sort O(n*log(n))

    for i in range(len_s - len_t + 1):
        if check_anagram(s[i: i+len_t], list_t):
            return True
    return False

def check_anagram(part_s, list_t):
    part_s = list(part_s)
    part_s.sort()   
    return part_s == list_t


print question1("udacity", "ud")
print question1("udacity", "")
print question1("udacity", "lp")

