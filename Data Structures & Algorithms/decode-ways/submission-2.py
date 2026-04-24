class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1

        def is_valid(s):
            if s[0] == '0':
                return False
            if not (0 < int(s) < 27):
                return False
            return True
        
        for idx in range(n-1, -1, -1):
            
            if is_valid(s[idx]):
                dp[idx] = dp[idx+1]
            
            if idx + 2 <= n and is_valid(s[idx:idx+2]) and dp[idx+2]:
                dp[idx] += dp[idx+2]
            
        return dp[0]
        