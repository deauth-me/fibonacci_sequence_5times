# generating Fibonacci sequence using class... time complexity O(n)

class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    # turning instances of this class into callable objects
    def __call__(self, n):
        if n < len(self.cache):
            return self.cache[n]
        else:
            fib_number = self(n-1) + self(n-2)
        self.cache.append(fib_number)

        return self.cache[n]


fibonacci_of = Fibonacci()

count = int(input("How many Fibonacci numbers do you want to generate? "))

fibonacci_list = [fibonacci_of(n) for n in range(count)]

print(fibonacci_list)
