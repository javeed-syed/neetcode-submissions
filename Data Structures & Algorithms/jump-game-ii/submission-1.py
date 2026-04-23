class Solution:
    def jump(self, nums: List[int]) -> int:
        res = float('inf')
        def solve(idx, curr):
            nonlocal res

            if idx >= len(nums):
                return

            if idx == len(nums) - 1:
                res = min(res, curr)
                return

            max_steps = nums[idx]

            for steps in range(1, max_steps + 1):
                solve(idx + steps, curr + 1)

        solve(0, 0)
        return res 