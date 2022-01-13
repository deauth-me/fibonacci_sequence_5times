# generating Fibonacci sequence using recursion

def fibonacci_of(n):
    if n in {0, 1}:
        return n

    return fibonacci_of(n - 1) + fibonacci_of(n - 2)


count = int(input("How many Fibonacci numbers do you want to generate? "))

fibonacci_list = [fibonacci_of(n) for n in range(count)]

print(fibonacci_list)
