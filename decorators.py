# 1
def start_end_mess(func):
    def inner_func(*args, **kwarg):
        print("Start function")
        func(*args, **kwarg)
        print("end function")
    return inner_func
    
# 2
import timeit
def time_measure(func):
    def timeing():
        start = timeit.timeit
        func()
        end = timeit.timeit
        print(f"the time the func take to run is {end - start} sec")
    return timeing
    
@time_measure
def greetings():
    print("hello how are you doing")
    
greetings()


# 3
def print_logs(func):
    def logs(*arg, **kwargs):
        for i in args:
            print(i)
    return logs
    
@print_logs
def greetings(*args):
    print("hello how are you doing")
    
greetings("a","b","c")


# 4
def apper_case(func):
    def string_received(*args, **kwargs):
        str_ = func(*args, **kwargs)
        if isinstance(str_,str):
            str_ = str_.upper()
        print(str_)
    return string_received
 
@apper_case   
def greetings(*args):
    print("hello how are you doing")
    str = ""
    for i in args:
        str += i
    return str
    
greetings("a","b","c")


# 5
def count_total(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        func(*args, **kwargs)
        print(f"the func was called {count} times")
    return inner
    
@count_total
def greetings(*args):
    print("hello how are you doing")

greetings()
greetings()
greetings()


# 6
def user_permission(func):
    def is_admin(is_admin):
        if is_admin == 123:
            func(is_admin)
        else:
            print(f"you have no admin permission")
    return is_admin
    
@user_permission
def check_password(password):
    print("hello sir how are you")
    
check_password(123)


# 7
# def check_duplicates(func):
#     old_args = None
#     old_kwargs = None
#     def remember_func(*args, **kwargs):
#         nonlocal old_kwargs, old_args
#         if not (old_args == args) and (old_kwargs == kwargs):
#             func(*args, **kwargs)
#         else:
#             return
#         old_args = args
#         old_kwargs = kwargs
#     return remember_func
    
# @check_duplicates
# def students(*names):
#     for i in names:
#         print(i)
        
# students("a","b","c")