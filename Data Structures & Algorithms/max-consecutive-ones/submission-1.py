class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = res = 0
        n = len(nums)
        for r in range(n):
            if nums[r] == 0:
                res = max(res, r-l)
                l = r+1
        return max(res, r-l+1)