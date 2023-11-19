input = [17, 13, 21, 19, 5]
print(input)

# διατήρηση της θέσης στην οποία βρίσκεται η κάθε τιμή του input
d = {}
for i, e in enumerate(input):
    d[e] = i

output = [0] * len(input)
for i, e in enumerate(sorted(d.keys())):
    output[d[e]] = i + 1

print(output)

# [17, 13, 21, 19, 5]
# [3, 2, 5, 4, 1]
