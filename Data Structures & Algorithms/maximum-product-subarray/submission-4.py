class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        mini = nums[0]
        maxi = nums[0]

        for curr in nums[1:]:
            v = (curr, curr*maxi, curr*mini)
            maxi = max(v)
            mini = min(v)
            res = max(res, maxi)
        return res