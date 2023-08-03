import time

def timer(func):

    def wrapper(x):
        start_time = time.time()
        ret = func(x)
        print(f"Time used: {time.time() - start_time}")
        return ret

    return wrapper

@timer
def my_func(x):
    time.sleep(x)

@timer
def double(x):
    return x * 2

my_func(2)
'''
my_func = timer(my_func) = wrapper
此时的wrapper定义为
def wrapper(x):
    start_time = time.time()
    ret = my_func(x)
    print(f"Time used: {time.time() - start_time}")
    return ret

my_func 和 wrapper 等价
最终执行的代码为
def wrapper():
    start_time = time.time()
    ret = time.sleep(2)
    print(f"Time used: {time.time() - start_time}")
'''
print(double(5))
'''
double = timer(double) = wrapper
此时的wrapper定义为
def wrapper(x):
    start_time = time.time()
    ret = double(x)
    print(f"Time used: {time.time() - start_time}")
    return ret
最终执行的代码为
def wrapper():
    start_time = time.time()
    ret = 5 * 2
    print(f"Time used: {time.time() - start_time}")
    return ret
print(ret)
'''