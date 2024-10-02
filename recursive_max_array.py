def max_array_r(a):
    if len(a) == 1:
        return a[0]
    else:
        return max(max_array_r(a[:-1]), a[-1])


if __name__ == "__main__":
    a = [4, 5, 2, 8, 1, 6]
    m = max_array_r(a)
    print(f"{a=}, max={m}")
