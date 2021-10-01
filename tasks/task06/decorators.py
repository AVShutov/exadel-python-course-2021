import time

def measure_elapsed_time(fn):
    def timer(*args, **kwargs):
        fn_name = fn.__name__
        print(f"Calling {fn_name}")
        start_time = time.perf_counter()
        value = fn(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"{fn_name} call took {run_time:.1f} seconds")
        return value
    return timer


@measure_elapsed_time
def my_fn1(arg1, arg2):
    time.sleep(0.5)
    return arg1 + arg2

@measure_elapsed_time
def my_fn2():
    time.sleep(0.8)
    print("I do nothing! What a life")

@measure_elapsed_time
def my_fn3(arg1, **kwargs):
    time.sleep(0.3)
    print(f"I also do nothing, but I have arg1 = {arg1} and kwargs = {kwargs}")

print("my_fn1 result:", my_fn1(1, 2))
my_fn2()
my_fn3(12, kwarg1='lol', kwarg2='kek')