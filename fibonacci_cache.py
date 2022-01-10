# generating Fibonacci sequence using cache...time complexity O(n)

cache = {0: 0, 1: 1}


def fibonacci_of(n):
    if n in cache:
        return cache[n]
    cache[n] = fibonacci_of(n-1) + fibonacci_of(n-2)
    return cache[n]


count = int(input("How many Fibonacci numbers do you want to generate? "))

fibonacci_list = [fibonacci_of(n) for n in range(count)]

print(fibonacci_list)
