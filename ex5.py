class Array_Queue:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.capacity = capacity
        self.size = 0
        self.tail = -1
        self.head = 0
        
    def empty(self):
        if self.size == 0:
            return "Empty"
        else:
            return "Not Empty"
        
    def full(self):
        if self.size == self.capacity:
            return "Full"
        else:
            return "Not Full"
    
    def peek(self):
        if self.size == 0:
            return "Peek None"
        else:
            return "Peek " + str(self.items[self.head])
        
    def enqueue(self, item):
        if self.size == self.capacity:
            return "Enqueue None"
        if self.size == 0:
            self.tail = 0
            self.head = 0
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % self.capacity
        else:
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % self.capacity 
        self.size += 1
        return "Enqueue " + str(item)
        
    def dequeue(self):
        if self.size == 0:
            return "Dequeue None"
        else:
            item = self.items[self.head]
            self.items[self.head] = None
            self.head = (self.head + 1) % self.capacity
            self.size -= 1
            return "Dequeue " + str(item)    
        
   
        

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LL_Queue:
    def __init__(self):
        self.head = None
        self.tail= None
        
    def enqueue(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        return "Enqueue " + str(value)
    
    def dequeue(self):
        if self.head is None:
            return "Dequeue None"
        value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        return "Dequeue " + str(value)
        
    def peek(self):
        if self.head is None:
            return "Peek None"
        return "Peek " + str(self.head.value)
    def empty(self):
        if self.head is None:
            return "Empty"
        else:
            return "Not Empty"
        
    def full(self):
        if self.head is None:
            return "Full"
        else:
            return "Not Full"
    
    




if __name__ == '__main__':
    Array_Queue = Array_Queue(7)
    print(Array_Queue.empty())
    print(Array_Queue.full())
    print(Array_Queue.enqueue(1))
    print(Array_Queue.enqueue(2))
    print(Array_Queue.enqueue(3))
    print(Array_Queue.peek())
    print(Array_Queue.enqueue(4))
    print(Array_Queue.enqueue(5))
    print(Array_Queue.enqueue(6))
    print(Array_Queue.peek())
    print(Array_Queue.enqueue(7))
    print(Array_Queue.dequeue())
    print(Array_Queue.dequeue())
    print(Array_Queue.peek())
    print(Array_Queue.dequeue())
    print(Array_Queue.peek())
    print(Array_Queue.dequeue())
    print(Array_Queue.dequeue())
    print(Array_Queue.peek())
    print(Array_Queue.dequeue())
    print(Array_Queue.peek())
    print(Array_Queue.enqueue(8))
    print(Array_Queue.peek())

    queue = LL_Queue()
    print(queue.enqueue(1))
    print(queue.enqueue(2))
    print(queue.enqueue(3))
    print(queue.enqueue(4))
    print(queue.enqueue(5))
    print(queue.enqueue(6))
    print(queue.enqueue(7))
    print(queue.enqueue(8))
    print(queue.peek())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.peek())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.peek())
    print(queue.enqueue(9))
    print(queue.peek())

    
    
        
        
   
        
        
    
