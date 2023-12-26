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

    def get(self, index):
        if index < 0 or index >= self.length :
            return None
        else:
            temp = self.head

            for _ in range(index):
                temp = temp.next
            return temp

myLinkedList = LinkedList(4)
myLinkedList.append(1)
myLinkedList.append(3)
myLinkedList.append(5)

print(myLinkedList.get(2).value)