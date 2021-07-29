# 6.Fibonacci Generator

def fibonacci():
    i = 0
    j = 1
    yield i
    yield j

    fibo_1 = j
    fibo_2 = i

    while True:
        fibo = fibo_1 + fibo_2
        yield fibo
        fibo_2 = fibo_1
        fibo_1 = fibo


generator = fibonacci()
for i in range(5):
    print(next(generator))
