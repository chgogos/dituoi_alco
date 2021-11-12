import random

random.seed(1234)
nums = random.sample(range(1, 1_000_000), 20_000)

sum = 1_000_000

nums = set(nums)
c = 0
for x in nums:
    if sum - x in nums:
        print(f"{x} + {sum-x} = {sum}")
        c += 1

print(f"{c//2} ζεύγη τιμών έχουν άθροισμα {sum}")
