def brute_force(a_list):
    """
    Find max subarray from a_list using brute force.
    """

    # initialize returns
    max_sum, start, end = a_list[0], 0, 0

    # brute force
    for i in range(len(a_list)):
        for j in range(i, len(a_list)):
            sum = 0
            for x in range(i, j + 1):
                sum += a_list[x]
            # replace starting and ending positions if a larger sum is found
            if max_sum < sum:
                max_sum, start, end = sum, i, j

    return max_sum, start, end


def prefix_sums_table_generator(a_list):
    """
    Generate prefix sums table for a_list
    """
    prefix_table = list()
    for index, num in enumerate(a_list):
        prefix_table.append(num if index == 0 else num + prefix_table[index - 1])
    return prefix_table


def prefix_sums(a_list):
    """
    Find max subarray from a_list using prefix sums.
    """
    # initialize returns
    max_sum, start, end = a_list[0], 0, 0

    # prefix table generation
    prefix_table = prefix_sums_table_generator(a_list)

    # use prefix table
    for i in range(len(a_list)):
        for j in range(i, len(a_list)):
            sum = prefix_table[j] if i == 0 else prefix_table[j] - prefix_table[i - 1]
            # replace starting and ending positions if a larger sum is found
            if max_sum < sum:
                max_sum, start, end = sum, i, j

    return max_sum, start, end


def kadane_table_generator(a_list):
    """
    Generate kadane table for a_list
    """
    kadane_table = list()
    for index, num in enumerate(a_list):
        sum = num if index == 0 else num + kadane_table[index - 1]
        kadane_table.append(0 if sum < 0 else sum)

    return kadane_table


def kadane(a_list):
    """
    Find max subarray from a_list using kadane algorithm.
    """
    # initialize returns
    max_sum, start, end = a_list[0], 0, 0

    # generate kadane table
    kadane_table = kadane_table_generator(a_list)

    # find max and ending position
    for index, sum in enumerate(kadane_table):
        if max_sum < sum:
            max_sum, end = sum, index

    # find starting position
    for i in range(end, 0, -1):
        if kadane_table[i] == 0:
            start = i + 1
            break

    return max_sum, start, end
