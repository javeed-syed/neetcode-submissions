class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def solve(idx):
            print(idx)
            if idx == len(nums) - 1:
                return True
            
            max_steps = nums[idx]

            curr = False
            for steps in range(1, max_steps + 1):
                curr = curr or solve(idx + steps)
            return curr
        return solve(0) 