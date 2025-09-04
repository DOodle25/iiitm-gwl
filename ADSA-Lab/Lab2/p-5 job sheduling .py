#  #! 5. Multi-Level Queue Scheduling with Priorities Design a system with two queues:
# # • Queue 1 → High-priority tasks (handled using a priority queue).
# # • Queue 2 → Normal tasks (handled using a FIFO queue).
# # Jobs arrive randomly with given priority, burst time, and arrival time.
# # • Execute all high-priority jobs first, then normal jobs in round robin order.
# # • Display execution order, waiting time, and turnaround time.

class job:
    def __init__(self, at, bt, p):
        self.at = at
        self.bt = bt
        self.p = p
        self.remaining_bt = bt
        self.completion_time = 0

class queue:
    def __init__(self):
        self.q = []
        # print(self.q)
        self.length = 0
    def __str__(self):
        return str(self.q)
    def enque(self, job):
        self.q.append(job)
        self.length += 1
        self.q.sort(key=lambda x: x.at)
        # print(self.q)
        return
    def deque(self):
        if self.length == 0:
            print("queue is empty")
            return None
        self.length -= 1
        return self.q.pop(0)

class priorityqueue:
    def __init__(self):
        self.pq = []
        # print(self.pq)
        self.length = 0
    def __str__(self):
        return str(self.pq)
    def enque(self, job):
        self.pq.append(job)
        self.length += 1
        self.pq.sort(key=lambda x: (x.p, x.at))
        # print(self.pq)
        return
    def deque(self):
        if self.length == 0:
            print("queue is empty")
            return None
        self.length -= 1
        return self.pq.pop(0)

class multileveljobsheduling:
    def __init__(self, quantum):
        self.pq = priorityqueue()
        self.q = queue()
        self.quantum = quantum
        self.time = -1
        self.ganttchart = []
    def add_job(self, job):
        if job.p > 0:
            self.pq.enque(job)
        else:
            self.q.enque(job)
    def schedule(self):
        self.time += 1
        while self.pq.length > 0 or self.q.length > 0:
            while self.pq.length > 0:
                current_job = self.pq.deque()
                if current_job.at > self.time:
                    self.time += 1
                    continue
                if current_job.bt <= self.quantum:
                    self.time += current_job.bt
                    self.ganttchart.append((self.time, current_job))
                else:
                    self.time += self.quantum
                    current_job.bt -= self.quantum
                    self.ganttchart.append((self.time, current_job))
                    self.pq.enque(current_job)
            while self.q.length > 0 and self.pq.length == 0:
                current_job = self.q.deque()
                if current_job.at > self.time:
                    self.time += 1
                    continue
                if current_job.bt <= self.quantum:
                    self.time += current_job.bt
                    self.ganttchart.append((self.time, current_job))
                else:
                    self.time += self.quantum
                    current_job.bt -= self.quantum
                    self.ganttchart.append((self.time, current_job))
                    self.q.enque(current_job)
        self.display_results()
    def display_results(self):
        print("Gantt Chart:")
        for time, job in self.ganttchart:
            print(f"Time {time}: Job {job.at} (BT: {job.bt}, P: {job.p})")
        print("\nAverage Waiting Time:", self.calculate_average_waiting_time())
        print("Average Turnaround Time:", self.calculate_average_turnaround_time())
    # def calculate_average_waiting_ime(self):
        # total_waiting_time = 0
        # for time, job in self.ganttchart:
            # total_waiting_time += time - job.at
        # return total_waiting_time / len(self.ganttchart)
    def calculate_average_turnaround_time(self):
        total_turnaround_time = 0
        for time, job in self.ganttchart:
            total_turnaround_time += time - job.at + job.bt
        return total_turnaround_time / len(self.ganttchart)

m = multileveljobsheduling(2)
m.add_job(job(0, 5, 1))
m.add_job(job(1, 3, 2))
m.add_job(job(2, 8, 0))
m.schedule()





