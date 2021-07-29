# 8.Get Primes

# def is_prime(number_in_sequence):
#     if number_in_sequence <= 1:
#         return False
#     for i in range(2, number_in_sequence):
#         if number_in_sequence % i == 0:
#             return False
#         return True


def get_primes(numbers):
    primes = filter(lambda n: is_prime(n), numbers)
    for numbers in primes:
        yield numbers


def is_prime(numbers):
    return numbers > 1 and all(numbers % i for i in range(2, numbers))


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
