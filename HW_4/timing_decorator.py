import time


def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        diff_time = end_time - start_time
        return diff_time

    return wrapper
