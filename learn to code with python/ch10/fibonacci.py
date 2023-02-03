import time

def fibonacci(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)


if __name__ == "__main__":
    for i in range(20, 55, 5):
        start = time.time()
        result = fibonacci(i)
        end = time.time()
        duration = end - start
        print(i, result, f'using {duration}second')