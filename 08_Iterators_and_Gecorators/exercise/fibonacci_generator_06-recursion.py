# 6.Fibonacci Generator with recursion

def fib():
    i = 0
    while True:
        yield fibonacci(i)
        i += 1


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


generator = fib()
for i in range(5):
    print(next(generator))
