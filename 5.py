from datetime import datetime
import time

def decorating_func(own_func):
    def wrapper(*args, **kwargs):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return own_func(*args, **kwargs)
    return wrapper

@decorating_func
def addition(num1, num2):
    return num1 + num2

print(addition(10, 5))

