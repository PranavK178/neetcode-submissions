class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for c in s:
            if c not in seen:
                seen[c] = 0
            seen[c] += 1
        for c in t:
            if c not in seen:
                return False
            seen[c] -= 1
        for letter in seen:
            if seen[letter] != 0:
                return False
        return True

        