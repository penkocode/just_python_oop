def type_check(type_param):
    def check_data_types(funk):
        def wrapper(arg):
            if type(arg) == type_param:
                return funk(arg)
            else:
                return "Bad Type"

        return wrapper

    return check_data_types


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
