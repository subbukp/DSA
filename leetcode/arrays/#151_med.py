'''
151. Reverse Words in a String:
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.strip().split()
        b = []
        for i in range(len(a)-1,-1,-1):
            b.append(a[i])
        return ' '.join(b).strip()

    def reverse_Words(self, s: str) -> str:
        words = []
        word = ""
        
        # Step 1: Extract words manually
        for ch in s:
            if ch != ' ':
                word += ch
            elif word:
                words.append(word)
                word = ""
        
        # If there’s a word left at the end, add it
        if word:
            words.append(word)
        # Step 2: Reverse manually
        result = ""
        for i in range(len(words) - 1, -1, -1):
            result += words[i]
            if i != 0:
                result += " "
        
        return result