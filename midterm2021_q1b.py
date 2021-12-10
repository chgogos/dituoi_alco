A = [1, 5, 6, 2, 7, 4]
d = 3

# O(n)
def print_pairs(A, d):
    s = set()
    for x in A:
        if x - d in s:
            print(x - d, x)
        if x + d in s:
            print(x, x + d)
        s.add(x)  # κάθε στοιχείο του A εισάγεται στο set


print_pairs(A, d)
