from queue import PriorityQueue

pq = PriorityQueue()
pq.put((1, "Task A"))
pq.put((1, "Task B"))
pq.put((1, "Task C"))

while not pq.empty():
    print(pq.get()[1])
from queue import PriorityQueue

schedule = PriorityQueue()
schedule.put((9, "Morning meeting"))
schedule.put((14, "Lunch with client"))
schedule.put((18, "Project review"))

while not schedule.empty():
    print(schedule.get()[1])
from queue import PriorityQueue

scores = PriorityQueue()
for s in [88, 95, 72, 99]:
    scores.put((-s, s))  # store negative for max-heap

while not scores.empty():
    print("Score:", scores.get()[1])
