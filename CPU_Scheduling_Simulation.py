import heapq

# Priority Queue
job_queue = []

# Current CPU job
current_job = None
remaining_time = 0

# Number of time slices (commands)
t = int(input("Enter number of time slices: "))

for time_slice in range(1, t + 1):
    print(f"\nTime Slice {time_slice}")

    command = input("Enter command: ").strip().lower()

    # Add job command
    if command.startswith("add"):
        name = input("Job Name: ")
        length = int(input("Job Length (1-100): "))
        priority = int(input("Priority (-20 to 19): "))

        heapq.heappush(job_queue, (priority, name, length))

    # If CPU is free, schedule next job
    if current_job is None and job_queue:
        priority, name, length = heapq.heappop(job_queue)
        current_job = name
        remaining_time = length

    # Execute current job
    if current_job:
        print("CPU Running:", current_job)
        remaining_time -= 1

        if remaining_time == 0:
            print(current_job, "completed.")
            current_job = None
    else:
        print("CPU Idle")

# Finish remaining jobs after commands are over
while current_job or job_queue:

    if current_job is None:
        priority, name, length = heapq.heappop(job_queue)
        current_job = name
        remaining_time = length

    print("\nCPU Running:", current_job)
    remaining_time -= 1

    if remaining_time == 0:
        print(current_job, "completed.")
        current_job = None