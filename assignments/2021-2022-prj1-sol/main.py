import random
import timeit
import matplotlib.pyplot as plt
from algorithms_max_sub_array import brute_force, prefix_sums, kadane


if __name__ == "__main__":
    functions = [brute_force, prefix_sums, kadane]

    # Create random lists
    num = [10, 100, 200, 500, 1000]
    random_lists = [[random.randint(-100, 100) for _ in range(n)] for n in num]

    # Benchmarks functions
    for f in functions:
        time_taken = list()
        for random_list in random_lists:
            start_time = timeit.default_timer()
            sum, start, end = f(random_list)
            duration = timeit.default_timer() - start_time
            print(f.__name__, len(random_list), f"{duration=} {sum=} {start=} {end=}")
            time_taken.append(duration)
        print()
        plt.plot(num, time_taken, label=f"{f.__name__}")

    # set matplotlib to log scale
    plt.xscale("log")
    plt.yscale("log")

    # label axis
    plt.xlabel("n")
    plt.ylabel("time")

    # show plot
    plt.legend()
    plt.show()
