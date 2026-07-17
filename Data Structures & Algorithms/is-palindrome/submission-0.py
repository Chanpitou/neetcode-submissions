class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = [c.lower() for c in list(s) if c.isalpha() or c.isdigit()]
        
        left, right = 0, len(new_s)-1
        while left < right:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1
        return True
        # return new_s == new_s[::-1]