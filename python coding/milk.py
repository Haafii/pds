from collections import deque

# Each milk packet has a name and manufacture date
class MilkPacket:
    def __init__(self, name, mfg_date):
        self.name = name
        self.mfg_date = mfg_date

    def __repr__(self):
        return f"{self.name} (MFG: {self.mfg_date})"

# Each box stores packets using stack (LIFO)
class Box:
    def __init__(self, box_id):
        self.box_id = box_id
        self.stack = []  # Stack list

    def add_packet(self, packet):
        self.stack.append(packet)  # Add to top

    def remove_packet(self):
        if self.stack:
            return self.stack.pop()  # Remove from top
        else:
            return "Box is empty"

    def show_packets(self):
        print(f"\nBox {self.box_id}:")
        for p in reversed(self.stack):  # Show top to bottom
            print(f"→ {p}")

# Create 3 boxes and store in a deque
boxes = deque()
for i in range(1, 4):
    boxes.append(Box(i))

# Add milk packets to each box
boxes[0].add_packet(MilkPacket("Milk1", "2025-07-20"))
boxes[0].add_packet(MilkPacket("Milk2", "2025-07-22"))

boxes[1].add_packet(MilkPacket("Milk3", "2025-07-18"))
boxes[1].add_packet(MilkPacket("Milk4", "2025-07-21"))

boxes[2].add_packet(MilkPacket("Milk5", "2025-07-19"))

# Show contents of each box
for box in boxes:
    box.show_packets()

# Example: Remove a milk packet from first box (stack behavior)
print("\nRemoved from Box 1:", boxes[0].remove_packet())
boxes[0].show_packets()
