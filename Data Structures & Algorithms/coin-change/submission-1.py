class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for amo in range(1, amount + 1):
            for coin in coins:
                if amo - coin > -1:
                    dp[amo] = min(dp[amo], 1 + dp[amo-coin])
        
        if dp[-1] == amount + 1:
            return -1
        else:
            return dp[-1]