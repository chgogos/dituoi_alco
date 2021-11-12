import random

N = 1_000_000  # πλήθος τιμών
M = 1_000_000  # εύρος ακεραίων τιμών από 1 μέχρι και Μ

random.seed(1234)
nums = [random.randint(1, M) for _ in range(N)]

nums = set(nums)
print(len(nums))