class Queue(object):
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def enqueue(self, data):
         return self.items.insert(0, data)

    def dequeue(self):
        return self.items.pop()


