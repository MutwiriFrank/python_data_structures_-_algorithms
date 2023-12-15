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

    def get(self, index):
        if index < 0 or index >= self.length :
            return None
        else:
            temp = self.head

            for _ in range(index):
                temp = temp.next
            return temp
        


    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -=1 
            if self.length == 0:
                self.tail = None
            


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
            


    def remove(self, index):

        if index < 0 or index > self.length :
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length-1 :
            return self.pop()
        
        pre = self.get(index-1)
        temp = self.get(index) # we wanna remove temp

        pre.next = temp.next
        temp.next = None

        self.length -= 1
        return temp


       




 



MyLinkedList =LinkedList(4) 
MyLinkedList.append(1)
MyLinkedList.append(15)
MyLinkedList.append(9)
MyLinkedList.remove(3)
MyLinkedList.print()

