import time
import random
import heapq

N = 10_000_000  # πλήθος τιμών
M = 1_000  # εύρος ακεραίων τιμών από 1 μέχρι και Μ
TOP = 10

random.seed(1234)
nums = [random.randint(1, M) for _ in range(N)]

my_map = {}
for k in nums:
    my_map[k] = my_map.get(k, 0) + 1

start_time = time.time()  # έναρξη χρονομέτρησης
hq = []
for v, freq in my_map.items():
    heapq.heappush(hq, (freq, v))
    if len(hq) > 10:
        heapq.heappop(hq)

while hq:
    freq, v = heapq.heappop(hq)
    print(f"{freq} εμφανίσεις της τιμής {v}")
print(f"{time.time() - start_time:.4f} δευτερόλεπτα")  # τερματισμός χρονομέτρησης
