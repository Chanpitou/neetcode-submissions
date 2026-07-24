class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1
        res = 1000
        while l <= r:
            if nums[l] >= nums[r]:
                res = min(res, nums[r])
            else:
                res = min(res, nums[l])
            l += 1
            r -= 1
        return res
