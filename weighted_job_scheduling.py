from bisect import bisect_right


def weighted_job_scheduling(jobs):
    # ταξινόμηση εργασιών με το χρόνο ολοκλήρωσης
    jobs.sort(key=lambda x: x[1])

    start_times = [job[0] for job in jobs]
    finish_times = [job[1] for job in jobs]
    profits = [job[2] for job in jobs]

    # η λίστα DP σε κάθε στοιχείο της αποθηκεύει το μέγιστο όφελος από τις εργασίες μέχρι το δείκτη του στοιχείου
    n = len(jobs)
    dp = [0] * n

    dp[0] = profits[0]

    for i in range(1, n):
        include_profit = profits[i]

        # Εύρεση της πλέον αργής μη-επικαλυπτόμενης εργασίας με δυαδική αναζήτηση
        index = bisect_right(finish_times, start_times[i]) - 1

        if index != -1:
            include_profit += dp[index]

        # Μέγιστο όφελος συμπεριλαμβάνοντας ή αποκλείοντας την τρέχουσα εργασία
        dp[i] = max(dp[i - 1], include_profit)

    print(dp)
    return dp[-1]


if __name__ == "__main__":
    # Λίστα εργασιών (start_time, end_time, profit)
    example_jobs = [
        (0, 5, 5),
        (2, 7, 3),
        (6, 11, 5),
        (4, 17, 4),
        (13, 23, 2),
        (24, 28, 5),
        (9, 30, 3),
    ]

    max_profit = weighted_job_scheduling(example_jobs)
    print(f"Maximum Profit: {max_profit}")
