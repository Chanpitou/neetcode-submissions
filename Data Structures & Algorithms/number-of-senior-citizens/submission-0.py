class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for d in details:
            curr_age = int(d[11:13])
            if curr_age > 60:
                ans += 1
        return ans