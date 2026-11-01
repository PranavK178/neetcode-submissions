class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        output = nums[r]
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= nums[r]:
                output = min(output, nums[m])
                r = m - 1
            else:
                l = m + 1
        return output