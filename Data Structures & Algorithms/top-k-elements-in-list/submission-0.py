from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)

        sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        return [sorted_dic[i][0] for i in range(k)]
