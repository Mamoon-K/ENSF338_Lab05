import timeit
import random
import matplotlib.pyplot as plt
#code by chatGPT
# Queue using Python arrays
class ArrayQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.insert(0, value)  # Insert at the head
    
    def dequeue(self):
        return self.queue.pop() if self.queue else None  # Remove from tail

# Queue using a singly-linked list
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def dequeue(self):
        if not self.head:
            return None
        if self.head == self.tail:  # Single element case
            value = self.tail.value
            self.head = self.tail = None
            return value
        
        curr = self.head
        while curr.next and curr.next != self.tail:
            curr = curr.next
        
        value = self.tail.value
        self.tail = curr
        self.tail.next = None
        return value

# Generate random tasks
def generate_tasks(n=10000):
    tasks = []
    for _ in range(n):
        op = "enqueue" if random.random() < 0.7 else "dequeue"
        value = random.randint(1, 1000) if op == "enqueue" else None
        tasks.append((op, value))
    return tasks

# Measure execution time
def measure_performance(queue_class, tasks):
    queue = queue_class()
    start_time = timeit.default_timer()
    for op, value in tasks:
        if op == "enqueue":
            queue.enqueue(value)
        else:
            queue.dequeue()
    return timeit.default_timer() - start_time

# Run experiments
array_times = []
linkedlist_times = []
for _ in range(100):
    task_list = generate_tasks()
    array_times.append(measure_performance(ArrayQueue, task_list))
    linkedlist_times.append(measure_performance(LinkedListQueue, task_list))

# Plot results


plt.hist(array_times, bins=20, alpha=0.5, label='Array Queue')
plt.hist(linkedlist_times, bins=20, alpha=0.5, label='Linked List Queue')
plt.xlabel("Execution Time (seconds)")
plt.ylabel("Frequency")
plt.legend()
plt.title("Performance Comparison of Queue Implementations")
plt.show()

# Discussion
print("Array-based queue is usually slower because inserting at the head is O(n), whereas in a linked list, it's O(1). ")
