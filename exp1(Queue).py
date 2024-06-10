#QUEUE
class QueueList:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from an empty queue")
    def size(self):
        return len(self.items)
# Testing the QueueList class
queue = QueueList()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.enqueue(10)
print("Front of the queue:", queue.peek())
print("Dequeue:", queue.dequeue())
print("Size of the queue:", queue.size())