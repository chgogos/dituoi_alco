def my_hash(s):
    t =0
    for i, c in enumerate(s):
        t += ord(c)*(i+1)^2
    return t % 101


print(my_hash("arta"))
print(my_hash("atra"))
print(my_hash("patra"))