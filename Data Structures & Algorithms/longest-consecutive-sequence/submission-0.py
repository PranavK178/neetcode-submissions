class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = {}
        for num in nums:
            if num not in sequence:
                sequence[num] = 0
        longest = 0
        temp = 0
        for num in sequence:
            check = num
            if (check - 1) not in sequence:
                while check in sequence:
                    temp += 1
                    check += 1
            if (temp > longest):
                longest = temp
            temp = 0
        return longest
        