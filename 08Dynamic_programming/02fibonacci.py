import re


def fibonacci(n):
    if n<2:
        return n

    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(6))


cache = {}
def fibbonacciMaster(n):
    if n in cache:
        return cache[n]
    else:
        if n<2:
            return n
        else:
            cache[n]=fibbonacciMaster(n-1)+fibbonacciMaster(n-2)
            return cache[n]