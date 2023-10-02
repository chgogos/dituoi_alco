import random


def flip_coin():
    if random.random() < 0.5:
        return "HEAD"
    else:
        return "TAIL"


def flip_coin_v2():
    return random.choice(["HEAD", "TAIL"])


def flip_biased_coin(bias=0.7):
    if random.random() < bias:
        return "HEAD"
    else:
        return "TAIL"


def scenario1():
    heads, tails = 0, 0
    N = 1_000_000
    for i in range(N):
        # if flip_coin() == "HEAD":
        # if flip_coin_v2() == "HEAD":
        if flip_biased_coin() == "HEAD":
            heads += 1
        else:
            tails += 1
    p_heads = heads / N * 100
    p_tails = tails / N * 100
    print(f"{p_heads=:.2f} {p_tails=:.2f}")


def scenario2():
    heads, tails = 0, 0
    N = 10000
    for i in range(N):
        while True:
            toss1 = flip_biased_coin()
            toss2 = flip_biased_coin()
            if toss1 != toss2:
                break
        if toss1 == "HEAD" and toss2 == "TAIL":
            heads += 1
        elif toss1 == "TAIL" and toss2 == "HEAD":
            tails += 1
    p_heads = heads / N * 100
    p_tails = tails / N * 100
    print(f"{p_heads=:.2f} {p_tails=:.2f}")


if __name__ == "__main__":
    # scenario1()
    scenario2()
