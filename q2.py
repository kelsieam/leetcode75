"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""


# def gcd_of_strings(s1, s2):
#     len1 = len(s1)
#     len2 = len(s2)
#     min_len = min(len1, len2)


#     divisor = ""

#     if s1 == s2:
#         return s2

#     elif s2 not in s1:
#         return ""

#     else:
#         for i in range(len(s1)):
#             count = 1
#             result = s2

#             while 


#     return divisor




# def gcdOfStrings(self, str1: str, str2: str) -> str:
#     L1, L2 = len(str1), len(str2)
#     L = min(L1, L2)
    
#     for x in range(L, 0, -1):
#         if L1%x!=0 or L2%x!=0: continue
#         candidate = str1[:x]
        
#         if candidate * (L1//x) == str1 and candidate * (L2//x) == str2:
#             return candidate
    
#     return ""



def gcd_of_strings(s1, s2):
    
    if s1 == s2:
        return s2

    if min(s1, s2) not in max(s1, s2):
        return ""
    
    len1 = len(s1)
    len2 = len(s2)
    min_len = min(len1, len2)

    if len1 % min_len != 0 or len2 % min_len != 0:
        return ""


    divisor = ""

    for i in range(min_len):
        count = 1
        result = s2

        while 


    return divisor


# s1 = "cat"
# s2 = "house"

# print(min(s1, s2))