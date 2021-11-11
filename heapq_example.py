import heapq

hq = [21, 5, 17, 12, 3, 9, 16]

heapq.heapify(hq) # MINHEAP

for _ in range(len(hq)):
    x = heapq.heappop(hq)
    print(x, end=" ")

# 3 5 9 12 16 17 21
