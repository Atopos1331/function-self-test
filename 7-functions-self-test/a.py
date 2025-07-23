
import time

def timer(target_function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = target_function(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Time consumed: {elapsed:.2f}s")
        return result
    return wrapper


@timer
def func():
    res = 0
    for i in range(100000000): res += i
    return res

func() # output: time consumed: 1.00s