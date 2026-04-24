class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def is_valid(s):
            if s[0] == '0':
                return False
            # if len(s) == 2 and s[0] == '0':
                # return False
            if not (0 < int(s) < 27):
                return False
            return True
        
        def solve(idx):
            if idx in memo:
                return memo[idx]

            if idx > n:
                return 0
            
            if idx == n:
                return 1
            
            res = 0

            if is_valid(s[idx]):
                res += solve(idx+1)

            if is_valid(s[idx: idx+2]):
                res += solve(idx+2)
            
            memo[idx] = res
            return res

        return solve(0)