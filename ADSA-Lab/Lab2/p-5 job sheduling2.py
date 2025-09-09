class Job:
    def __init__(self, at, bt, p, name):
        self.name = name
        self.at = at
        self.bt = bt
        self.p = p
        self.remaining_bt = bt
        self.completion_time = 0

class Queue:
    def __init__(self):
        self.q = []
    def enque(self, job):
        self.q.append(job)
        self.q.sort(key=lambda x: x.at)
    def deque(self):
        if not self.q:
            return None
        return self.q.pop(0)
    def __len__(self):
        return len(self.q)

class PriorityQueue:
    def __init__(self):
        self.pq = []
    def enque(self, job):
        self.pq.append(job)
        self.pq.sort(key=lambda x: (x.p, x.at))
    def deque(self):
        if not self.pq:
            return None
        return self.pq.pop(0)
    def __len__(self):
        return len(self.pq)

class MultiLevelJobScheduling:
    def __init__(self, quantum):
        self.pq = PriorityQueue()
        self.q = Queue()
        self.quantum = quantum
        self.time = 0
        self.ganttchart = []
        self.jobs = []
    def add_job(self, job):
        self.jobs.append(job)
        if job.p > 0:
            self.pq.enque(job)
        else:
            self.q.enque(job)
    def schedule(self):
        current_job = None
        while any(job.remaining_bt > 0 for job in self.jobs):
            for job in self.jobs:
                if job.at == self.time and job.remaining_bt > 0:
                    if job.p > 0 and job not in self.pq.pq:
                        self.pq.enque(job)
                    elif job.p == 0 and job not in self.q.q:
                        self.q.enque(job)

            # P
            if len(self.pq) > 0:
                self.pq.pq.sort(key=lambda x: (x.p, x.at))
                next_job = self.pq.pq[0]
                if current_job is None or next_job.p < current_job.p or current_job.remaining_bt == 0:
                    current_job = next_job
                self.time += 1
                current_job.remaining_bt -= 1
                self.ganttchart.append((self.time, current_job.name))
                if current_job.remaining_bt == 0:
                    current_job.completion_time = self.time
                    self.pq.pq.remove(current_job)
                    current_job = None

            # Np
            elif len(self.q) > 0:
                current_job = self.q.deque()
                if current_job.at > self.time:
                    self.time = current_job.at
                exec_time = min(self.quantum, current_job.remaining_bt)
                self.time += exec_time
                current_job.remaining_bt -= exec_time
                self.ganttchart.append((self.time, current_job.name))
                if current_job.remaining_bt == 0:
                    current_job.completion_time = self.time
                else:
                    self.q.enque(current_job)
                current_job = None
            else:
                self.time += 1

        self.display_results()
    def display_results(self):
        print("Gantt Chart:")
        for time, name in self.ganttchart:
            print(f"Time {time}: {name}")

        total_wt, total_tat = 0, 0
        n = len(self.jobs)
        print("\nJob Results:")
        for job in self.jobs:
            tat = job.completion_time - job.at
            wt = tat - job.bt
            total_tat += tat
            total_wt += wt
            print(f"{job.name}: AT={job.at}, BT={job.bt}, P={job.p}, CT={job.completion_time}, TAT={tat}, WT={wt}")

        print(f"\nAverage Waiting Time = {total_wt/n:.2f}")
        print(f"Average Turnaround Time = {total_tat/n:.2f}")

m = MultiLevelJobScheduling(quantum=2)
m.add_job(Job(0, 5, 1, "J1"))
m.add_job(Job(1, 3, 2, "J2"))
m.add_job(Job(2, 8, 0, "J3"))
m.schedule()
