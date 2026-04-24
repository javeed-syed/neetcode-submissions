class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        n = len(nums)
        for i in range(n):
            curr = None
            for j in range(i, n):
                if not curr:
                    curr = nums[j]
                else:
                    curr *= nums[j]
                res = max(res, curr)
        return res