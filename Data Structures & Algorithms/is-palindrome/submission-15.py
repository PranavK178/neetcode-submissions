class Solution:
    def isPalindrome(self, s: str) -> bool:
        # left = 0
        # right = len(s) - 1
        # while left < right:
        #     while not s[left].isalnum():
        #         left += 1
        #         if left >= right:
        #             return True
        #     while not s[right].isalnum():
        #         right -= 1
        #         if right <= left:
        #             return True
        #     if s[left].lower() != s[right].lower():
        #         return False
        #     left += 1
        #     right -= 1
        # return True
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not (s[l]).isalnum():
                l += 1
            while r > l and not (s[r]).isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True