class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = [")", "]", "}"]
        for char in s:
            if len(stack) == 0:
                if char in closed:
                    return False
                else:
                    stack.append(char)
            elif char == ")":
                if stack.pop() != "(":
                    return False
            elif char == "]":
                if stack.pop() != "[":
                    return False
            elif char == "}":
                if stack.pop() != "{":
                    return False
            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        return False
        
