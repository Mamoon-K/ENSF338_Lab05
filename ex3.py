import random
import timeit
import matplotlib.pyplot as plt


# Stack using Python List (Array-Based Stack)
class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()


# Stack using Singly Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        return value


# Function to generate a random task list
def generate_task_list(size=10000):
    task_list = []
    for _ in range(size):
        if random.random() < 0.7:
            task_list.append(("push", random.randint(1, 1000)))
        else:
            task_list.append(("pop", None))
    return task_list


# Function to execute a task list on a given stack implementation
def run_test(stack_class, task_list):
    stack = stack_class()
    for task, value in task_list:
        if task == "push":
            stack.push(value)
        else:
            stack.pop()


# Measure performance
def measure_performance():
    task_lists = [generate_task_list() for _ in range(100)]

    array_times = [timeit.timeit(lambda: run_test(ArrayStack, task_list), number=1) for task_list in task_lists]
    linked_list_times = [timeit.timeit(lambda: run_test(LinkedListStack, task_list), number=1) for task_list in
                         task_lists]

    # Plot results
    plt.hist(array_times, bins=30, alpha=0.5, label='Array-Based Stack')
    plt.hist(linked_list_times, bins=30, alpha=0.5, label='Linked List Stack')
    plt.xlabel("Time (seconds)")
    plt.ylabel("Frequency")
    plt.title("Stack Performance Comparison")
    plt.legend()
    plt.show()

    print(f"Array-Based Stack Average Time: {sum(array_times) / len(array_times):.5f} seconds")
    print(f"Linked List Stack Average Time: {sum(linked_list_times) / len(linked_list_times):.5f} seconds")


# Run performance measurement
measure_performance()

"""
Discussion:
- Array-based stack is typically faster due to O(1) push/pop operations using Python's dynamic array.
- Linked list stack has O(1) push/pop, but incurs extra memory overhead for node pointers.
- The histogram shows distribution differences, with arrays generally performing better.
"""