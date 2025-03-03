import sys

# Assumptions:
"""
We assume that there will only be single digit operands since in the material given this is how they are presented.
This also must be true for this to work for the given inputs in the lab such as (+15) = 6 since there is no way
to differentiate if that means 15 or 1 and 5 unless we specify.
Additionally, we assume that the left most operand is the one that is put first in operations 
where order matters like subtraction or division. Ex. (/ 6 3) = 6 / 3 = 2
Lastly, we assumed division was integer division
"""

class Stack():
    def __init__(self):
        self.arr = []
        self.top = -1

    def push(self, value):
        self.top += 1
        self.arr.append(value)

    def pop(self):
        if (self.top <= -1):
            return None
        removed = self.arr[self.top] 
        self.top -= 1
        self.arr.pop()

        return removed
    
    def peek(self):
        if (self.top <= -1):
            return None
        return self.arr[self.top]
    
    def isEmpty(self):
        if (self.top <= -1):
            return True
        return False

# Created with help from ChatGPT based on an original attempt
def tokenize(expression):
    """Converts the input string into tokens (numbers, operators, parentheses)."""
    tokens = []

    # Since we treat each digit as a number, we simply append them if they are a digit or a character in our accepted list.
    for char in expression:
        if char.isdigit() or char in "()+-*/":
            tokens.append(char)
    
    return tokens

def evaluate(tokens):
    """Evaluates the tokenized expression using a stack."""
    if len(tokens) == 1 and tokens[0].isdigit():
        return int(tokens[0])  # If there's only a number, return it directly

    stack = Stack()
    
    # If there are no parentheses, then there is 1 operation so do that.
    if "(" not in tokens and ")" not in tokens:
        operator = tokens[0]
        num1 = int(tokens[1])
        num2 = int(tokens[2])

        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            return num1 // num2  
        
    # Otherwise, go through all the tokens
    for token in tokens:
        if token.isdigit():
            stack.push(int(token))
        elif token in "+-*/":
            stack.push(token)
        elif token == ")":
            # Evaluate expression inside parentheses
            operands = Stack()
            # If you have hit a closing parentheses, then go towards the left (using the stack) until you hit the opening parentheses
            while not stack.isEmpty() and stack.peek() != "(":
                operands.push(stack.pop())
            stack.pop()  # Remove '(' since we just peeked it leaving it on the stack.

            operator = operands.pop()
            
            # Reverse order of operands to ensure correct calculation
            # Ie, the leftmost operand is the first evaluated
            num1 = operands.pop()
            num2 = operands.pop()

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 // num2
            
            stack.push(result)

        else:  # Opening parentheses
            stack.push(token)

    return stack.pop()

# Read input
argsInRaw = " ".join(sys.argv[1:])
tokens = tokenize(argsInRaw)

# Evaluate and print result
print(evaluate(tokens))
