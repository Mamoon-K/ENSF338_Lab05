import sys
from random import randint

#1
class Stack:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.capacity = capacity
        self.size = 0
        self.tail = 0
        self.head = self.tail
        
    
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
        
    def enqueue(self, item):
        if self.size == self.capacity:
            return "Enqueue None"
            
        if self.size == 0:
            self.tail = 0
            self.head = 0
            self.tail = (self.tail + 1) % self.capacity
            self.items[self.tail] = item
            self.size += 1
            return "Enqueue " + str(item)    
        else:
            self.tail = (self.tail + 1) % self.capacity
            self.items[self.tail] = item
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
        
        
    def peek(self):
        if self.size == 0:
            return "Peek None"
        else:
            return "Peek " + str(self.items[self.head])
    


if __name__ == '__main__':
    stack = Stack(5)
    print(stack.empty())
    print(stack.full())
    print(stack.enqueue(1))
    print(stack.enqueue(2))
    print(stack.enqueue(3))
    print(stack.enqueue(4))
    print(stack.enqueue(5))
    print(stack.enqueue(6))
    print(stack.dequeue())
    print(stack.dequeue())
    print(stack.dequeue())
        
        
        
        
        
    
