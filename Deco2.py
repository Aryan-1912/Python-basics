def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say():
    list = [1,2,3]
    for i in list:
        print(i, end="")

print(say())

import os

print(os.getcwd())