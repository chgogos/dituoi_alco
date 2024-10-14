def max_r(a):
    if len(a) == 1:
        return a[0]
    else:
        print(f"a={a[:-1]}, last={a[-1]}")
        return max(max_r(a[:-1]), a[-1])


a = [4, 2, 7, 8, 1, 9, 0]
print(max_r(a))
