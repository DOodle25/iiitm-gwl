# 1. Activity Selection (Given start and end times)
def activity_selection(jobs):
    # jobs: list of (start, end)
    jobs.sort(key=lambda x: x[1])  # sort by end time
    selected = []
    last_end = -float('inf')
    for start, end in jobs:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

# 2. Weighted Interval Scheduling (Given length and weight, no start time)
def weighted_job_scheduling(jobs):
    # jobs: list of (length, weight)
    # Assume jobs can be scheduled one after another (no overlap)
    jobs.sort(key=lambda x: -x[1]/x[0])  # sort by weight/length ratio
    scheduled = []
    time = 0
    for length, weight in jobs:
        scheduled.append((time, time+length, weight))
        time += length
    return scheduled

# 3. Weighted Interval Scheduling (Given start, end, weight)
def weighted_interval_scheduling(jobs):
    # jobs: list of (start, end, weight)
    jobs.sort(key=lambda x: x[1])  # sort by end time
    n = len(jobs)
    # Compute p(j): last job before j that doesn't overlap
    p = [0]*n
    for j in range(n):
        p[j] = -1
        for i in range(j-1, -1, -1):
            if jobs[i][1] <= jobs[j][0]:
                p[j] = i
                break
    # DP
    dp = [0]*n
    for j in range(n):
        incl = jobs[j][2]
        if p[j] != -1:
            incl += dp[p[j]]
        dp[j] = max(incl, dp[j-1] if j > 0 else 0)
    # Recover solution
    def find_solution(j):
        if j < 0:
            return []
        incl = jobs[j][2] + (dp[p[j]] if p[j] != -1 else 0)
        if incl > (dp[j-1] if j > 0 else 0):
            return find_solution(p[j]) + [jobs[j]]
        else:
            return find_solution(j-1)
    return find_solution(n-1)

# Example usage:
if __name__ == "__main__":
    # 1. Activity Selection
    jobs1 = [(1,4), (3,5), (0,6), (5,7), (8,9), (5,9)]
    print("Activity Selection:", activity_selection(jobs1))

    # 2. Weighted Job Scheduling (length, weight)
    jobs2 = [(3,10), (1,5), (2,8)]
    print("Weighted Job Scheduling (no overlap):", weighted_job_scheduling(jobs2))

    # 3. Weighted Interval Scheduling (start, end, weight)
    jobs3 = [(1,3,5), (2,5,6), (4,6,5), (6,7,4), (5,8,11), (7,9,2)]
    print("Weighted Interval Scheduling:", weighted_interval_scheduling(jobs3))