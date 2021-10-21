# Πλήθος βημάτων που απαιτούνται για την εκτέλεση της συνάρτησης fact: 5n + 2


def fact(n):
    result = 1  # 1 βήμα
    while n > 1:  # n βήματα
        result *= n  # 2 * n βήματα
        n -= 1  # 2 * n βήματα
    return result  # 1 βήμα


print(fact(10))
