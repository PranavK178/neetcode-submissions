class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        height = []
        index = []
        height.append(heights[0])
        index.append(0)
        largest = height[0]
        count = 0
        temp_index = []
        for i in range(1, len(heights)):
            largest = max(largest, heights[i])
            while heights[i] < height[-1]:
                temp_index.append(index.pop())
                largest = max(largest, (i - temp_index[-1]) * height.pop())
                count += 1
                if not height:
                    break
            for j in range(count):
                height.append(heights[i])
                index.append(temp_index[j])
            height.append(heights[i])
            index.append(i)
            count = 0
            temp_index.clear()
        while height:
            largest = max(largest, (len(heights) - index.pop()) * height.pop())
        
        return largest
            