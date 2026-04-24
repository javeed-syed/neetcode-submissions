class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        n = len(nums)
        for i in range(n):
            curr = 1
            for j in range(i, n):
                curr *= nums[j]
                res = max(res, curr)
        return res