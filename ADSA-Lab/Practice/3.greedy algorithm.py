# Disk Scheduling Algorithms

# Each disk request is represented as a dictionary:
# {'id': int, 'size': int, 'length': int, 'frequency': int}

requests = [
    {'id': 1, 'size': 500, 'length': 10, 'frequency': 5},
    {'id': 2, 'size': 200, 'length': 20, 'frequency': 10},
    {'id': 3, 'size': 800, 'length': 5, 'frequency': 2},
    {'id': 4, 'size': 300, 'length': 15, 'frequency': 8},
]

# 1. Schedule by decreasing size
def schedule_by_size(requests):
    return sorted(requests, key=lambda x: x['size'], reverse=True)

# 2. Schedule by decreasing length
def schedule_by_length(requests):
    return sorted(requests, key=lambda x: x['length'], reverse=True)

# 3. Schedule by decreasing frequency
def schedule_by_frequency(requests):
    return sorted(requests, key=lambda x: x['frequency'], reverse=True)

print("Schedule by decreasing size:")
for req in schedule_by_size(requests):
    print(req)

print("\nSchedule by decreasing length:")
for req in schedule_by_length(requests):
    print(req)

print("\nSchedule by decreasing frequency:")
for req in schedule_by_frequency(requests):
    print(req)