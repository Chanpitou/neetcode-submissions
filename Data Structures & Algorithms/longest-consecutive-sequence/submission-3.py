class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        sorted_num = sorted(nums)
        ans = 1
        cnt = 1
        for i in range(1, len(sorted_num)):
            if sorted_num[i] == sorted_num[i-1] + 1:
                cnt += 1
                ans = max(ans, cnt)
            elif sorted_num[i] == sorted_num[i-1]:
                continue
            else:
                cnt = 1
        return ans