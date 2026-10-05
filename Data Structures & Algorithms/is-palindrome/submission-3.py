class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        s = s.lower()
        new = ""
        for c in s:
            if c.isalnum():
                new += c
        right = len(new) - 1
        while left < right:
            if left == right:
                break
            if new[left] != new[right]:
                print(new[left])
                print(new[right])
                return False
            left += 1
            right -= 1
        return True