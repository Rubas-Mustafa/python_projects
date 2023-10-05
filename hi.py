
# class MyQueue:

def __init__(self):
        self.stack1 = []
        self.stack2 = []

def push(self, x: int) -> None:
        self.stack1.append(x)
        # print(x)
        # print(self.stack1)
        # print(self.stack2)

def transfer(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
            # print(self.stack2)

def pop(self) -> int:
        if not self.stack2: #this means if stack 2 is empty
            self.transfer() #start transfering the elements from stack1 to stack 2
        return self.stack2.pop()
        
def peek(self) -> int:
        if not self.stack2:
            self.transfer()
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2
