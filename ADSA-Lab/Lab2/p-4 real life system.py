class Job:
    def __init__(self, name, at, bt):
        self.name = name
        self.at = at
        self.bt = bt
        self.rt = bt
        
class RoundRobin:
    def __init__(self, qt):
        self.qt = qt
        self.jobs = []
        self.gantt = []
        self.averagewaiting = 0
        self.turnaround = 0
        self.completion = 0

    def __str__(self):
        for i in self.jobs:
            print(i.at, i.bt)
        return "done"

    def jobpost(self, job):
        self.jobs.append(job)

    # def run(self):
    #     while any(job.rt > 0 for job in self.jobs):
    #         for job in self.jobs:
    #             if job.rt > 0:
    #                 if job.rt > self.qt:
    #                     job.rt -= self.qt
    #                     self.completion += self.qt
    #                 else:
    #                     self.completion += job.rt
    #                     job.rt = 0
    #                 self.gantt.append((job.name, job.at, self.completion))
    #     self.calculate_metrics()

    def run(self):
        time = 0
        ready_queue = []
        jobs = sorted(self.jobs, key=lambda x: x.at)
        jobs_left = jobs.copy()
        while jobs_left or ready_queue:
            # arrived check
            while jobs_left and jobs_left[0].at <= time:
                ready_queue.append(jobs_left.pop(0))
            if ready_queue:
                job = ready_queue.pop(0)
                exec_time = min(self.qt, job.rt)
                self.gantt.append((job.name, time, time + exec_time))
                time += exec_time
                job.rt -= exec_time
                if job.rt > 0:
                    # during check
                    while jobs_left and jobs_left[0].at <= time:
                        ready_queue.append(jobs_left.pop(0))
                    ready_queue.append(job)
                else:
                    job.completion_time = time
            else:
                time += 1
        self.completion = time
        self.calculate_metrics()


    def calculate_metrics(self):
        self.averagewaiting = sum([self.completion - job.at - job.bt for job in self.jobs]) / len(self.jobs)
        self.turnaround = self.completion / len(self.jobs)

rb = RoundRobin(3)
rb.jobpost(Job("a", 1,7))
rb.jobpost(Job("b", 3,5))
rb.jobpost(Job("c", 2,3))
rb.jobpost(Job("d", 4,1))
rb.jobpost(Job("e", 5,4))
print(rb)
rb.run()
print(rb.gantt)
print(rb.averagewaiting)
print(rb.turnaround)
print(rb.completion)