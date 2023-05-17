class mQueue:
    def __init__(self):
        self.queue = []

    def put(self, item):
        self.queue.append(item)
        return True

    def get(self):
        item = self.queue[0]
        self.queue.remove(item)
        return item

    def remove(self, item):
        if item not in self.queue:
            return False
        self.queue.remove(item)
        return True

    def show(self):
        return self.queue

    def empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False


    def get_element(self, item):
        if item not in self.queue:
            return False
        else:
            for elem in self.queue:
                if elem == item:
                    self.queue.remove(item)
                    return elem


#test

# q = Queue()
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# while not q.empty():
#     print(q.show())
#     print(q.get())

