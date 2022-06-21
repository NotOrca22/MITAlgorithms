class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
class Linkedlist:
    def __init__(self):
       self.head = None
       self.last_node = None
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end = ' ')
            curr = curr.next
myList = Linkedlist()
for i in [1,69,340,42,59,99]:
    myList.append(i)
myList.display()