A = [1, 5, 6, 2, 7, 4]
d = 3

# O(n^2)
def print_pairs(A, d):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if abs(A[i] - A[j]) == d:
                if A[i] < A[j]:
                    print(A[i], A[j])
                else:
                    print(A[j], A[i])


print_pairs(A, d)
