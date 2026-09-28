class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        temp1 = 1
        temp2 = 1
        for i in range(len(tokens)):
            if tokens[i] == "+":
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(temp1 + temp2)
            elif tokens[i] == "-":
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(temp2 - temp1)
            elif tokens[i] == "/":
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(int(temp2 / temp1))
            elif tokens[i] == "*":
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(temp1 * temp2)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
