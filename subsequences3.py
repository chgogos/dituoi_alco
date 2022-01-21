subsequences = []

def all_subsequences(string, index, c):
    if index == len(string):
        if c != '':
            subsequences.append(c)
        return
    all_subsequences(string, index + 1, c + string[index])
    all_subsequences(string, index + 1, c)


all_subsequences("ΤΑΞΗ", 0, "")
print(subsequences)
