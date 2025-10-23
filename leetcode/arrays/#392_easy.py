'''
392. Is Subsequence:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p,flag = 0,0
        if not s:
            return True
        for i in t:
            if i == s[p]:
                p+=1
                if len(s)==p:
                    return True
        return False