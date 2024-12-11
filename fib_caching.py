F = [None] * 101
F[0] = 0
F[1] = 1


def fib_c(n):
    if F[n] is None:
        F[n] = fib_c(n - 1) + fib_c(n - 2)
    return F[n]


r = fib_c(100)
print(r)
