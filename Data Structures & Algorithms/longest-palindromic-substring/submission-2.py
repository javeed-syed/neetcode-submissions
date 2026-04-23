class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_str = s[0]
        max_len = 1

        for i in range(n):
            l, r = i - 1, i + 1
            while l > -1 and r < n and s[l] == s[r]:
                if r-l+1 > max_len:
                    max_len = r-l+1
                    max_str = s[l:r+1]
                l -= 1
                r += 1

            l, r = i, i + 1
            while l > -1 and r < n and s[l] == s[r]:
                if r-l+1 > max_len:
                    max_len = r-l+1
                    max_str = s[l:r+1]
                l -= 1
                r += 1
        
        return max_str