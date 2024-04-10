# https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(self.min, val)
        

    def pop(self) -> None:
        if self.stack:
            popped_ele = self.stack.pop()
            if popped_ele == self.min:
                self.min = min(self.stack) if self.stack else float('inf')

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min if self.stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()