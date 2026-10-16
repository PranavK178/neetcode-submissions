class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        most = 0
        temp = 0
        while left < right:
            temp = min(heights[left], heights[right]) * (right - left)
            most = max(temp, most)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return most