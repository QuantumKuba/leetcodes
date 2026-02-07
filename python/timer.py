import time
import functools

def time_execution(func):
    """
    Decorator to measure the execution time of a function.
    Prints the time in milliseconds.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"Function '{func.__name__}' took {execution_time:.4f} ms")
        return result
    return wrapper
