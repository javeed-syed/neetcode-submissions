class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = nums[0]

        for num in nums[1:]:
            curr = max(0, curr)
            curr += num
            res = max(curr, res)
        return res