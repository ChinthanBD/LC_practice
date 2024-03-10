class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.next = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        elif self.count == 0:
            self.count += 1
            return 0
        elif self.count == 1:
            self.count += 1
            return 1
        else:
            fib = self.current + self.next
            self.current, self.next = self.next, fib
            self.count += 1
            return fib

# Example usage:
n = 4
fibonacci = FibonacciIterator(n)
for num in fibonacci:
    print(num, end=' ')