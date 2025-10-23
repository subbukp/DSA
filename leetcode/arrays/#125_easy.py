'''
125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''
class Solution:
    def is__Palindrome(self, s: str) -> bool:
        '''
        my solution
        '''
        p0=0
        s1 = ''
        for i in s:
            if i.isalnum():
                s1+=i.lower()
        p1=len(s1)-1
        while p0<p1:
            if s1[p0] != s1[p1]:
                return False
            p0+=1
            p1-=1
        return True


    def isPalindrome(self, s: str) -> bool:
        def is_alnum(ch):
            # manually check if character is a-z, A-Z, or 0-9
            if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9'):
                return True
            return False

        # extract only alphanumeric characters in lowercase
        filtered = []
        for ch in s:
            if is_alnum(ch):
                filtered.append(ch.lower())

        # check palindrome manually using two pointers
        left, right = 0, len(filtered) - 1
        while left < right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def is_Palindrome(self, s: str) -> bool:
        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
        return filtered == filtered[::-1]