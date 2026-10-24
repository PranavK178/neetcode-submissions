class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = height[0]
        rightMax = height[right]
        water = 0
        while left < right:
            if leftMax < rightMax:
                if height[left] < leftMax:
                    water += leftMax - height[left]
                left += 1
                leftMax = max(leftMax, height[left])
            else:
                if height[right] < rightMax:
                    water += rightMax - height[right]
                right -= 1
                rightMax = max(rightMax, height[right])
        return water

             
            
            
