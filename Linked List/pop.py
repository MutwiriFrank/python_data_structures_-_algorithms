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
        
        
        if self.length == 0:
            return None
        
        pre = self.head
        temp = self.head

        # for _ in range(self.length - 1)
        while temp.next is not None:
            pre = temp
            temp = temp.next 
        
        self.tail = pre
        self.tail.next = None
        self.length -= 1
              
        
        if self.length == 0:
            self.head = None
            self.tail = None
            self.length = 0
            
        return temp   
        
    
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