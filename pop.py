class Node:
    def __init__(self, value):
        self.value =value
        self.next = None


class LinkedList:
    def __init__(self, value) :
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
            self.tail.next  = new_node 
            self.tail = new_node
        
        self.length += 1


    def pop(self):
        # when length = 0
        if self.length == 0:
            return None
        temps = self.head
        pre = self.head 
        # while length is 2 or more
        while temps.next is not None :
            pre = temps
            temps = temps.next        
        self.tail = pre
        self.tail.next = None
        self.length -=1
        # when the length is just 1
        if self.length == 0:
            self.head = None
            self.head = None
        
    
        return temps
            

MyLinkedList =LinkedList(4) 
MyLinkedList.append(3)
MyLinkedList.append(1)
print('popped', MyLinkedList.pop().value)

# print(MyLinkedList.pop().value)
# print(MyLinkedList.pop().value)
# print(MyLinkedList.pop().value)
# print(MyLinkedList.pop())
# MyLinkedList.print_list()


MyLinkedList.print_list()