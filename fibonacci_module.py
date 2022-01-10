# generating Fibonacci sequence with Python module gmpy2
# you might need to pip install gmpy2

from gmpy2 import fib

count = int(input("How many Fibonacci numbers do you want to generate? "))

fibonacci_list = [int(fib(n)) for n in range(count)]

print(fibonacci_list)
