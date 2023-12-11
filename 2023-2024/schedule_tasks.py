def schedule_tasks(tasks):
    tasks.sort(key=lambda x: x[0])

    # List to store the end time of the last task on each machine
    machines = []

    for task in tasks:
        scheduled = False
        for i in range(len(machines)):
            # If the task can be scheduled on the machine
            if machines[i] <= task[0]:
                machines[i] = task[1]  # Update the end time of the machine
                scheduled = True
                break

        # If the task cannot be scheduled on any existing machine, add a new machine
        if not scheduled:
            machines.append(task[1])

    return len(machines), machines

# Given tasks
tasks = [[1, 4], [1, 3], [2, 5], [3, 7], [4, 7], [6, 9], [7, 8]]

# Schedule tasks and get the minimum number of machines needed
min_machines, machine_end_times = schedule_tasks(tasks)
min_machines, machine_end_times
