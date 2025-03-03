import random
import timeit


class PriorityQueueSort:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
        self.queue = self.merge_sort(self.queue)

    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


class PriorityQueueInsert:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        if not self.queue:
            self.queue.append(value)
        else:
            for i in range(len(self.queue)):
                if value < self.queue[i]:
                    self.queue.insert(i, value)
                    return
            self.queue.append(value)

    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop(0)


def generate_task_list(size=1000):
    task_list = []
    for _ in range(size):
        if random.random() < 0.7:
            task_list.append(("enqueue", random.randint(1, 1000)))
        else:
            task_list.append(("dequeue", None))
    return task_list


def run_test(pq_class, task_list):
    pq = pq_class()
    for task, value in task_list:
        if task == "enqueue":
            pq.enqueue(value)
        else:
            pq.dequeue()


def measure_performance():
    task_lists = [generate_task_list() for _ in range(100)]

    sort_time = timeit.timeit(lambda: [run_test(PriorityQueueSort, task_list) for task_list in task_lists], number=1)
    insert_time = timeit.timeit(lambda: [run_test(PriorityQueueInsert, task_list) for task_list in task_lists],
                                number=1)

    print(f"PriorityQueueSort time: {sort_time:.5f} seconds")
    print(f"PriorityQueueInsert time: {insert_time:.5f} seconds")


# Measure performance
measure_performance()

"""
Discussion:
- PriorityQueueSort: Enqueue is O(n log n) due to mergesort, dequeue is O(1).
- PriorityQueueInsert: Enqueue is O(n) due to sorted insert, dequeue is O(1).
- Since enqueue occurs 70% of the time, PriorityQueueInsert is generally faster.
"""
