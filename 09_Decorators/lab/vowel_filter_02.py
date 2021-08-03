# 2.Vowel Filter


def vowel_filter(function):
    def wrapper():
        return [el for el in function() if el.lower() in "AOUEIYaoueiy"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
