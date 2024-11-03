import random


def hash_function1(k, N):
    return k % N


def hash_function2(k):
    return 7 - k % 7


# ΚΕΦΑΛΑΙΟ 6Β - ΔΙΑΦΑΝΕΙΑ 15
def linear_probing_example():
    print("OPEN ADDRESSING - LINEAR PROBING EXAMPLE")
    keys = [18, 41, 22, 44, 59, 32, 31, 73]
    N = 13  # size of hashtable

    # Open addressing, linear probing example
    for k in keys:
        h = hash_function1(k, N)
        print(f"key{k}, hash={h}")


def quadratic_probing_example():
    print("OPEN ADDRESSING - QUADRATIC PROBING EXAMPLE")
    keys = [18, 41, 22, 44, 59, 32, 31, 73]
    N = 13  # size of hashtable

    # Open addressing, quadratic probing example
    for k in keys:
        h = hash_function1(k, N)
        hs = [(h + i**2) % N for i in range(5)]
        print(f"key={k}, hash={h}, hash_positions={hs}")


# ΚΕΦΑΛΑΙΟ 6Β - ΔΙΑΦΑΝΕΙΑ 26
def double_hashing_example():
    print("OPEN ADDRESSING - DOUBLE HASHING EXAMPLE")
    keys = [18, 41, 22, 44, 59, 32, 31, 73]
    N = 13  # size of hashtable

    # Open addressing, double hashing example
    for k in keys:
        h1 = hash_function1(k, N)
        h2 = hash_function2(k)
        h1_h2s = [(h1 + i * hash_function2(k)) % N for i in range(1, 10)]
        print(f"key={k}, hash1={h1}, hash2={h2}, hash positions={[h1]+h1_h2s}")


def random_hashing_example():
    print("OPEN ADDRESSING - RANDOM HASHING")
    keys = [18, 41, 22, 44, 59, 32, 31, 73]
    N = 13  # size of hashtable
    seed = 424242
    random.seed(seed)
    # Open addressing, random hashing example
    for k in keys:
        h = hash_function1(k, N)
        rs = [random.randint(0, N - 1) for i in range(5)]
        hs = [h] + [(h + i) % N for i in rs]
        print(f"key={k}, hash={h}, random={rs}, hash_positions={hs}")


if __name__ == "__main__":
    linear_probing_example()
    quadratic_probing_example()
    double_hashing_example()
    random_hashing_example()
