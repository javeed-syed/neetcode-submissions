class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def solve(idx, balance):
            if (idx, balance) in memo:
                return memo[(idx, balance)]
                
            if balance < 0:
                return False
            
            if idx == len(s):
                return balance == 0
            
            ch = s[idx]

            if ch == '(':
                ans = solve(idx + 1, balance + 1)
            elif ch == ')':
                ans = solve(idx + 1, balance - 1)
            else:
                ans = (solve(idx + 1, balance + 1) or
                solve(idx + 1, balance) or
                solve(idx + 1, balance - 1))
            
            memo[(idx, balance)] = ans
            return ans

        return solve(0, 0)