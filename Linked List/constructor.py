class Node:
    # s node has value and next
    def __init__(self, value):
        self.value = value
        self.next = None


class MyLinkedList:

    def __init__(self, value) :
        new_node = Node(value)
        # head and tail are also nodes
        self.head = new_node
        self.tail = new_node
        self.length = 1

ll = MyLinkedList(4)

print(ll.head.value)