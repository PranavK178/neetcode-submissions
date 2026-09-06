class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        start = 1
        temp = 0
        temp_freq = 0
        output = []
        while start <= k:
            for c in count:
                if count[c] > temp_freq:
                    temp = c
                    temp_freq = count[c]
            output.append(temp)
            count[temp] = 0
            start += 1
            temp = 0
            temp_freq = 0
        return output