def fib_ultimate(n):
    if n == 0:
        return 0
    back2, back1 = 0, 1
    for i in range(2, n):
        next = back1 + back2
        back2 = back1
        back1 = next
    return back1 + back2


r = fib_ultimate(6)
print(r)
