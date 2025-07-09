class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.size() > 0:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def empty(self):
        return self.size() == 0


if __name__ == '__main__':
    s = Stack()
    print(s.peek())
    print(s.empty())