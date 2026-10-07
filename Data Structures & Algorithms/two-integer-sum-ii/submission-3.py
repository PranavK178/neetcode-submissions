class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sumCheck = numbers[left] + numbers[right]
            if sumCheck == target:
                return [left + 1, right + 1]
            if sumCheck < target:
                left += 1
            if sumCheck > target:
                right -= 1
        
        
