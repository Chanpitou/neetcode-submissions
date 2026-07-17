class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        sorted_nums = sorted(set(nums))
        ans = 1
        cnt = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1] + 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
        return ans