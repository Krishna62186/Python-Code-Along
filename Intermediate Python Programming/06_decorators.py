# 06 - Decorators
# A decorator wraps a function to add behaviour.

import time

def announce(function):
    def wrapper(*args, **kwargs):
        print("Starting function...")
        result = function(*args, **kwargs)
        print("Function finished.")
        return result
    return wrapper

@announce
def greet(name):
    print(f"Hello, {name}!")

greet("Asha")

# A timing decorator
def measure_time(function):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{function.__name__} took {elapsed:.6f} seconds")
        return result
    return wrapper

@measure_time
def calculate_sum(limit):
    return sum(range(limit))

print("Sum:", calculate_sum(1_000_000))
