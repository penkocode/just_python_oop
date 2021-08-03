# 4. Multiply
def multiply(times):
    def decorator(ref_function):
        def wrapper(num):
            result = ref_function(num)
            return result * times

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))
