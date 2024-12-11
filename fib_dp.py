def fib_dp(n):
    F = [None] * (n + 1)
    F[0], F[1] = 0, 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]


r = fib_dp(6)
print(r)
