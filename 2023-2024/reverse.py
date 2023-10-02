def reverse(a):
    N=len(a)
    for i in range(N//2):
        a[i], a[N-1-i] = a[N-1-i], a[i]
    return a 

import time

start = time.time() 
a = list(range(50000))
for i in range(1000):
    reverse(a)

elapsed_time = time.time() -start

print(elapsed_time)