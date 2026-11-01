class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        output = r
        while l <= r:
            k = (r + l) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / k)
            if time <= h:
                r = k - 1
                output = k
            else:
                l = k + 1
        return output