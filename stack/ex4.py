class MyQueue:

    def __init__(self):
        self.stack1 = []  # Стек для додавання елементів
        self.stack2 = []  # Стек для вилучення елементів

    def push(self, x: int):
        self.stack1.append(x)

    def pop(self) -> int:
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()

    def peek(self) -> int:
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2[-1]

    def empty(self) -> bool:
        
        return not self.stack1 and not self.stack2


# Тестування:
queue = MyQueue()
queue.push(1)  # Черга: [1]
queue.push(2)  # Черга: [1, 2]
print(queue.peek())  # Повертає 1
print(queue.pop())   # Повертає 1, черга: [2]
print(queue.empty())  # Повертає false, оскільки в черзі є елемент
