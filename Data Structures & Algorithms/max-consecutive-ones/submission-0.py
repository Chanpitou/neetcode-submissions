class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = res = 0
        for num in nums:
            if num == 0:
                res = max(res, count)
                count = 0
            else:
                count += 1
        return max(res, count)