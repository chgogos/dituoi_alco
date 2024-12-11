from functools import lru_cache


@lru_cache(maxsize=None)
def fib_r(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_r(n - 1) + fib_r(n - 2)


r = fib_r(50)
print(r)
