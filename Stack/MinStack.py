from collections import deque

class MinStack:

    """
    We create Two stack one of them reponsable for our stack
    second one responsable for tracking minimal stack.
    And we just .append() into our MinStack minimal value 
    between of top-value and bottom-value,
    so it's like .append(min(val, minStack[-1])) 
    """

    def __init__(self):
        self.stack = deque()
        self.minStack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(
                min(val, self.minStack[-1])
                )
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    
if __name__ == "__main__":
    actions =["MinStack","push","push","push","getMin","pop","top","getMin"]
    values = [[],[-2],[0],[-3],[],[],[],[]]
    obj = MinStack()

    obj.push([-2])
    obj.push([0])
    obj.push([-3])

    print("Get min before: ", obj.getMin())
    obj.pop()
    print("Top: ", obj.top())
    print("Get min after: ", obj.getMin())