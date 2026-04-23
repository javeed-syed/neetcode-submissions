class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        count = 0
        for i in range(n):
            dp[i][i] = True
            count += 1
            for j in range(i):
                l = i - j + 1
                if s[i] == s[j] and (l < 4 or dp[j+1][i-1]):
                    dp[j][i] = True
                    count += 1

        return count