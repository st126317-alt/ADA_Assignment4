# Weighted Interval Scheduling (Dynamic Programming)

jobs = [
    {"id": "J1", "start": 1, "finish": 4, "reward": 5},
    {"id": "J2", "start": 3, "finish": 5, "reward": 2},
    {"id": "J3", "start": 0, "finish": 6, "reward": 8},
    {"id": "J4", "start": 4, "finish": 7, "reward": 6},
    {"id": "J5", "start": 3, "finish": 8, "reward": 7},
]

# Step 1: Sort jobs by finish time
jobs_sorted = sorted(jobs, key=lambda x: x["finish"])

# Step 2: Compute p(j) for each job
def compute_p(jobs):
    p = []
    for j in range(len(jobs)):
        pred = -1
        for i in range(j-1, -1, -1):
            if jobs[i]["finish"] <= jobs[j]["start"]:
                pred = i
                break
        p.append(pred)
    return p

p = compute_p(jobs_sorted)

# Step 3: DP table
n = len(jobs_sorted)
OPT = [0] * (n+1)  # OPT[0] = 0

for j in range(1, n+1):
    incl = jobs_sorted[j-1]["reward"] + OPT[p[j-1]+1]
    excl = OPT[j-1]
    OPT[j] = max(incl, excl)

# Step 4: Reconstruct solution
def find_solution(j):
    if j == 0:
        return []
    if jobs_sorted[j-1]["reward"] + OPT[p[j-1]+1] > OPT[j-1]:
        return find_solution(p[j-1]+1) + [jobs_sorted[j-1]]
    else:
        return find_solution(j-1)

selected_jobs = find_solution(n)

# Show results
print("Optimal reward:", OPT[n])
print("Selected jobs:")
for job in selected_jobs:
    print(f"{job['id']} (start={job['start']}, finish={job['finish']}, reward={job['reward']})")
