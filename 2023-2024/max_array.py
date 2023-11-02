def maximum_r_wrapper(a):
    return maximum_r(a, len(a))

# T(n) = 3 αν n == 1
# T(n) = T(n-1) + 7 αν n > 1
# μη αναδρομική σχέση: T(n) = 7n-4
def maximum_r(a, n):
    if n == 1:
        return a[0]
    else:
        return max(maximum_r(a, n - 1), a[n - 1])

# T(n) = 7n - 2 worst case
# T(n) = 5n best case
def maximum(a,n):
    current_max = a[0] # +2
    i = 1 # +1
    while i < n: # +n
        if a[i] > current_max: # +2(n-1)
            current_max = a[i] # +2(n-1)
        i += 1 # +2(n-1)
    return current_max # +1

if __name__ == "__main__":
    a = [2, 3, 56, 34, 12, 19]
    m = maximum(a, len(a))
    print("Λύση με επανάληψη: ", m)
    m = maximum_r_wrapper(a)
    print("Λύση με αναδρομή: ", m)
