class circularqueue:
    def __init__(self, length):
        self.cq = [None for _ in range(length)]
        print(self.cq)
        self.sp = 0
        self.ep = 0
        self.length = length
        self.count = 0

    def __str__(self):
        return str(self.cq)

    def enque(self, val):
        if self.count == self.length:
            print("queue is full")
        else:
            self.cq[self.sp] = val
            self.sp = (self.sp + 1) % self.length
            self.count += 1
        print(self.cq)

    def deque(self):
        if self.count == 0:
            print("queue is empty")
            return None
        val = self.cq[self.ep]
        self.cq[self.ep] = None
        self.ep = (self.ep + 1) % self.length
        self.count -= 1
        print(self.cq)
        return val
        
    def peek(self):
        if self.count == 0:
            print("queue is empty")
            return None
        return self.cq[self.ep]

cq = circularqueue(5)
cq.enque(1)
cq.enque(2)
cq.enque(3)
cq.enque(4)
cq.enque(5)
cq.enque(6)
cq.enque(7)
print("Dequeued:", cq.deque())
# print("Peek:", cq.peek())
cq.enque(8)
cq.enque(9)
print("Dequeued:", cq.deque())
print("Dequeued:", cq.deque())
print("Dequeued:", cq.deque())
print("Dequeued:", cq.deque())
print("Dequeued:", cq.deque())
print("Dequeued:", cq.deque())
print("Dequeued:", cq.deque())
print("Dequeued:", cq.deque())
