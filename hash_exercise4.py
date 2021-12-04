input = [17, 13, 21, 19, 5]
print(input)

# διατήρηση της θέσης στην οποία βρίσκεται η κάθε τιμή του input
d = {}
for i,e in enumerate(input):
    d[e] = i

rank = 1    
for e in sorted(d.keys()):
    input[d[e]] = rank
    rank += 1
    
print(input)

# [17, 13, 21, 19, 5]
# [3, 2, 5, 4, 1]