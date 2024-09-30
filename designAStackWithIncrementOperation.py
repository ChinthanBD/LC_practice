# https://leetcode.com/problems/design-a-stack-with-increment-operation/?envType=daily-question&envId=2024-09-30
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = list()        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        return self.stack.pop()
        

    def increment(self, k: int, val: int) -> None:
        upto = min(k, len(self.stack))
        for i in range(upto):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
