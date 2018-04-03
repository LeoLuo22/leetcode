class MyStack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        data = self.data[-1]
        self.data = self.data[0:len(self.data)-1]
        return data

    def top(self):
        if self.empty():
            return []
        return self.data[-1]

    def empty(self):
        return True if len(self.data) == 0 else False

    def show(self):
        print(self.data)

def main():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    print(stack.top())
    stack.show()

if __name__ == '__main__':
    main()
