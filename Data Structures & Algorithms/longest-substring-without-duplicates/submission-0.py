from collections import defaultdict, deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = deque()
        res = 0

        for right in range(len(s)):
            while queue and s[right] in queue:
                queue.popleft()
            queue.append(s[right])
            res = max(res, len(queue))

        return res
