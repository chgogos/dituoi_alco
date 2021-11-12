import heapq  # MINHEAP

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

max_hq = []
min_hq = []

for i, x in enumerate(nums):
    heapq.heappush(max_hq, -x)
    if len(min_hq) > 0 and -max_hq[0] > min_hq[0]:
        t = heapq.heappop(max_hq)
        heapq.heappush(min_hq, -t)
    if len(max_hq) - len(min_hq) == 2:
        t = heapq.heappop(max_hq)
        heapq.heappush(min_hq, -t)
    elif len(min_hq) - len(max_hq) == 2:
        t = heapq.heappop(min_hq)
        heapq.heappush(max_hq, -t)
    if len(max_hq) == len(min_hq):
        median = (-max_hq[0] + min_hq[0]) / 2
    elif len(max_hq) > len(min_hq):
        median = -max_hq[0]
    else:
        median = min_hq[0]
    print(f"items processed={nums[:i+1]} - median={median:.2f}")
