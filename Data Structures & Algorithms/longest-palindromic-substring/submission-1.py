class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        is_palindrome = lambda s: s == s[::-1]
        max_str = s[0]
        max_len = 1

        for l in range(n):
            for r in range(l, n+1):
                if r-l > max_len and is_palindrome(s[l:r]):
                    max_len = r - l
                    max_str = s[l:r]
        
        return max_str