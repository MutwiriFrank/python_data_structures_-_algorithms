#  node
#  constructor
# print
#  append


class Node:
    # node = value + next

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # ll = head+ tail + length

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1

        else:
            # first set tail. next to new node then move the tail poilnter to the newly added node
            self.tail.next  =new_node
            self.tail= new_node

        self.length += 1
 



MyLinkedList =LinkedList(4) 
MyLinkedList.append(1)
MyLinkedList.print()

