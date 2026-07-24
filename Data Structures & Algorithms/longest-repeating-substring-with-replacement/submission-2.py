class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = curr_max = res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            curr_max = max(curr_max, count[s[r]])

            while (r-l+1) - curr_max > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res