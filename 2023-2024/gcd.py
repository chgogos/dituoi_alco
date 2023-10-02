import time
from random import randrange


def gcd_naive(x, y):
    z = min(x, y)
    for i in range(z, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def gcd_r(x, y):
    if y == 0:
        return x
    return gcd_r(y, x % y)


if __name__ == "__main__":
    start = time.time()
    for _ in range(10000):
        a = randrange(5000, 20000)
        b = randrange(5000, 20000)
        # x = gcd_naive(a,b)
        # x = gcd(a, b)
        x = gcd_r(a, b)
    elapsed_time = time.time() - start
    print(f"Elapsed time {elapsed_time:.4f}")
