class Solution:
    def maxScore(self, s: str) -> int:
        temp = 0
        left = 0
        longest = 0
        while left < len(s) - 1:
            temp = s[:left + 1].count("0") + s[left + 1:].count("1")
            longest = max(temp,longest)
            if len(s[left:]) == 1:
                break
            left += 1
            temp = 0
        return longest

