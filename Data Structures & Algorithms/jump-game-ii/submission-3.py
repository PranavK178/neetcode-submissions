class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = [float('inf')] * (len(nums))
        steps[0] = 0
        right = 0
        left = 0
        for i in range(len(nums)):
            left = i + 1
            if (i + nums[i]) > (len(nums) - 1) or i + 1 > (len(nums) - 1):
                if i < len(nums) - 1 and i + nums[i] > len(nums) - 1:
                    steps[len(nums) - 1] = min(steps[i] + 1, steps[len(nums) - 1])
                continue
            right = i + nums[i]
            while left <= right:
                steps[left] = min(steps[i] + 1, steps[left])
                print(steps[left])
                left += 1  
        print(steps)
        return steps[(len(nums) - 1)]

            
