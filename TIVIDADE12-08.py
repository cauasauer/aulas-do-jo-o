class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
pilha = Stack()

pilha.push('500')
pilha.push('300')
pilha.push('150')
print(pilha.items)
print(pilha.peek())
print(pilha.items)
pilha.pop()
print(pilha.items)