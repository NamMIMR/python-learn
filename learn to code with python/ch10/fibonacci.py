import time

def fibonacci(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def dict_fib(num: int) -> int:
    fib_dict = {}
    for i in range(num+1):
        if i == 0:
            fib_dict[i] = 0
        elif i == 1:
            fib_dict[i] = 1
        else:
            fib_dict[i] = fib_dict[i-1] + fib_dict[i-2]
    return fib_dict[num]

cache = {}
def fib2(num: int) -> int:
    global cache
    if num in cache:
        return cache[num]
    
    if num == 0:
        result = 0
    elif num == 1:
        result = 1
    else:
        result = fib2(num-1) + fib2(num-2)
    cache[num] = result
    return result

if __name__ == "__main__":
    start = time.time()
    for i in range(0, 101):
        
        # result = fibonacci(i)
        result = dict_fib(i)
    end = time.time()
    duration = end - start
    print(f'using {duration} seconds')

    start = time.time()
    for i in range(0, 101):
        
        # result = fibonacci(i)
        result = fib2(i)
    end = time.time()
    duration = end - start
    print(f'fib2 using {duration} seconds')