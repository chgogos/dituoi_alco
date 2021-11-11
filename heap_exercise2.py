import random
import heapq  # MINHEAP

# N = 10_000_000  # πλήθος τιμών
# M = 1_000  # εύρος ακεραίων τιμών από 1 μέχρι και Μ

# random.seed(1234)
# nums = [random.randint(1, M) for _ in range(N)]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

max_hq = (
    []
)  # το max_hq δέχεται τις τιμές με αρνητικό πρόσημο έτσι ώστε να λειτουργήσει ως MAXHEAP

min_hq = []

if nums[0] > nums[1]:
    max_hq.append(nums[1])
    min_hq.append(nums[0])
else:
    max_hq.append(nums[0])
    min_hq.append(nums[1])

for i, x in enumerate(nums[2:]):
    heapq.heappush(
        max_hq, -x
    )  # Process integer from the stream and add it to the max heap.
    if -max_hq[0] > min_hq[0]:
        t = heapq.heappop(max_hq)
        heapq.heappush(min_hq, -t)
    if len(max_hq) - len(min_hq) > 1:
        t = heapq.heappop(max_hq)
        heapq.heappush(min_hq, -t)
    elif len(min_hq) - len(max_hq) > 1:
        t = heapq.heappop(min_hq)
        heapq.heappush(max_hq, -t)
    if len(max_hq) == len(min_hq):
        median = (-max_hq[0] + min_hq[0]) / 2
    elif len(max_hq) > len(min_hq):
        median = -max_hq[0]
    else:
        median = min_hq[0]
    print(f"items processed={nums[:i+3]} - median={median:.2f}")
