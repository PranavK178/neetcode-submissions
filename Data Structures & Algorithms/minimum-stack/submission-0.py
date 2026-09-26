class MinStack:

    def __init__(self):
        self.stack = []
        self.stackmn = []

    def push(self, val: int) -> None: 
        self.stack.append(val)
        if self.stackmn:
            val = min(val, self.stackmn[-1])
        self.stackmn.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stackmn.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackmn[-1]
        
