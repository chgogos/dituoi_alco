def all_subsequences(s):
    subsequences = []
    for i in range(1, 2 ** len(s)):
        subsequence = []
        for k in range(len(s)):
            if i & (1 << k):  # είναι 1 το k-οστό bit του i?
                subsequence.append(s[k])
        subsequences.append("".join(subsequence))
    return subsequences


subsequences = all_subsequences("ΤΑΞΗ")
print(subsequences)