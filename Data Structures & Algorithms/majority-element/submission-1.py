from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        curr = None
        for key, value in freq.items():
            if freq[key] > freq[curr]:
                curr = key
        return curr