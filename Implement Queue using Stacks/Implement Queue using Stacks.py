class MyQueue:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        data = self.data[0]
        self.data.remove(data)
        return data

    def peek(self):
        return self.data[0]

    def empty(self):
        return True if len(self.data) == 0 else False

    def show(self):
        print(self.data)
def main():
    queue = MyQueue()
    queue.push(1)
    queue.push(1)
    queue.push(2)
    queue.show()
    print(queue.peek())
    print(queue.pop())
    queue.show()

if __name__ == '__main__':
    main()
