from functools import wraps


# def outside_function(some_number):
#     def separator(symbol, number):
#         print(symbol * number)
#     separator("*", 23)
#     print(f"Executing for number {some_number}")
#     separator("*", 23)
#     return some_number * 2
#
# result1 = outside_function(5)
# print(result1)

# def hello():
#     print("Hello")
#
# def hi():
#     print("hi")
#
# def welcome():
#     print("welcome")
#
# def greeting_function(callback):
#     print("text before greeting")
#     callback()
#     print("text after greeting")
#
# greeting_function(hello)
# greeting_function(hi)

# def greet(callback):
#     def wrapper():
#         print("text before")
#         callback()
#         print("text after")
#     return wrapper
# @greet
# def hello():
#     print("Hello")
#
# hello()

# from functools import wraps
#
# def dectorator_base_without_arguments(callback):
#     @wraps(callback)
#     def wrapper():
#         callback()
#     return wrapper
## @decorator_base_without_arguments
# def example_without_arguments():
#     print("hello")
#
# example_without_arguments()

def decorator_base_with_arguments(callback):
    @wraps(callback)
    def wrapper(*args, **kwargs):
        callback(*args, **kwargs)
    return wrapper

@decorator_base_with_arguments
def example(first, second):
    print(first + second)

example(23,12)