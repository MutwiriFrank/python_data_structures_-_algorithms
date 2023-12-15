class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next =None


class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
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
            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1


    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
        self.length += 1
        return True



myLL = LinkedList(5)
myLL.append(1)
myLL.append(2)
myLL.prepend(8)
myLL.print_list()