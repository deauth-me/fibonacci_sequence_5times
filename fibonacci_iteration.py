# generating Fibonacci sequence using iteration

def fibonacci_of(n):
    if n in {0, 1}:
        return n

    previous, fib_number = 0, 1

    for i in range(n):
        previous, fib_number = fib_number, previous + fib_number

    return fib_number


count = int(input("How many Fibonacci numbers do you want to generate? "))

fibonacci_list = [fibonacci_of(n) for n in range(count)]

print(fibonacci_list)
