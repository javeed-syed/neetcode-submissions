class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        res = s[0]
        max_len = 1

        is_palindrome = lambda x: x == x[::-1]

        for i in range(len(s)):
            for j in range(i + max_len + 1, len(s) + 1):
                if is_palindrome(s[i:j]):
                    max_len = j - i
                    res = s[i:j]
        
        return res
