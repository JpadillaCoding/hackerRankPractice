class MinStack:
    def __init__(self):
        self.myStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.myStack.append(val)
        self.minStack.append( val if not self.minStack else min(val, self.minStack[-1]))
    def pop(self) -> None:
        self.myStack.pop()
        self.minStack.pop()
    def top(self) -> int:
        return self.myStack[-1]
    def getMin(self) -> int:
        return self.minStack[-1]
    
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.push(4)
minStack.getMin()
minStack.pop()
minStack.top()    
minStack.getMin()