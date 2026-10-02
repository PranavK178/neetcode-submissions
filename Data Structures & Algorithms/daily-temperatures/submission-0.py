class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        index = []
        output = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1] :
                temp_index = index.pop()
                print(temp_index)
                output[temp_index] = i - temp_index
                stack.pop() 
            stack.append(temp)
            index.append(i)
        return output
            
            

            
            
