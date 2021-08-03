# # Class Logger
# from datetime import datetime
#
#
# class func_logger:
#     _logfile = 'out.log'
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args):
#         log_string = self.func.__name__ + " was called" + ' : ' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#         with open(self._logfile, 'a') as opened_file:
#             opened_file.write(log_string + '\n')
#         return self.func(*args)
from datetime import datetime


def func_logger(ref_func):
    def wrapper(name):
        with open("log.txt", "a") as file:
            file.write(f'{ref_func.__name__} was called : {str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}\n')
        return ref_func(name)

    return wrapper


@func_logger
def say_hi(name):
    print(f"Hi, {name}")


@func_logger
def say_bye(name):
    print(f"Bye, {name}")


say_hi("Peter")
say_bye("Peter")
