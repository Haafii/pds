from collections import deque

# Create a class for Bread
class Bread:
    def __init__(self, name, expiry):
        self.name = name
        self.expiry = expiry  # expiry in days

    def __repr__(self):
        return f"{self.name} (Expiry: {self.expiry})"

# Bread Queue class
class BreadQueue:
    def __init__(self):
        self.queue = deque()

    def add_bread(self, bread):
        # Insert in increasing order of expiry
        i = 0
        while i < len(self.queue) and self.queue[i].expiry <= bread.expiry:
            i += 1
        self.queue.insert(i, bread)

    def serve_bread(self):
        if self.queue:
            return self.queue.popleft()  # Bread with earliest expiry
        else:
            return "No bread to serve."

    def show_queue(self):
        print("Bread Queue (Earliest Expiry First):")
        for b in self.queue:
            print(b)

# 🔄 Example
bq = BreadQueue()
bq.add_bread(Bread("BreadA", 3))
bq.add_bread(Bread("BreadB", 1))
bq.add_bread(Bread("BreadC", 5))
bq.add_bread(Bread("BreadD", 2))

bq.show_queue()
print("\nServing:", bq.serve_bread())
bq.show_queue()
