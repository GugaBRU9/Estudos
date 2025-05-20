class MinStack:
    def __init__(self):
        self.stack = []
        self.m = [float('inf')]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.m[-1]:
            self.m.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.m[-1]:
            self.m.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.m[-1]

s = MinStack()
s.push(2)
s.push(0)
s.push(3)
s.push(0)
print(s.getMin())
s.pop()
print(s.getMin())
s.pop()
print(s.getMin())
s.pop()
print(s.getMin())
