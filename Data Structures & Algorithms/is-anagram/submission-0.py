from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = Counter(s)
        dic2 = Counter(t)

        if dic1.keys() != dic2.keys():
            return False

        if sorted(dic1.values()) != sorted(dic2.values()):
            return False
        return True