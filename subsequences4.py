from itertools import combinations


def all_subsequences(s):
    out = []
    for r in range(1, len(s) + 1):
        for c in combinations(s, r):
            out.append("".join(c))
    return out


subsequences = all_subsequences("ΤΑΞΗ")
print(subsequences)
