
class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)
        print("Pushed",item)

    def pop(self):
        pop_element = self.items.pop()
        return pop_element

    def display(self):

        for item in reversed(self.items):
            print(item)     

stack =Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print("pop element : ",stack.pop())

stack.display()