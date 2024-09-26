class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    

class LinkedList:
    def __init__(self, head=None):
        self.head = head


    def print(self):    
        current = self.head
        while True:
            if current == None:
                print("")
                break
            else:
                print(current.data,  end='')
                current = current.next_node
            if current != None:
                print(" ->", end='')
                if current != None:
                    print(" ", end='')
    
    def append(self, num):
        n = Node(num)
        if self.head == None:
            self.head = n
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = n

    def insert(self, num, id):
        current = self.head
        n = Node(num)
        if id == 0:
            n.next_node = self.head 
            self.head = n
        else:
            while id > 1:
                current = current.next_node
                id -= 1
            next = current.next_node
            current.next_node = None
            current.next_node = n
            n.next_node = next

    def delete(self,id):
        count = 0
        current = self.head
        while True:
            if current == None:
                break
            else:
                count += 1
                current = current.next_node
        current = self.head

        if id >= count:
            return None
        
        if id < count:
            if id == 0:
                deleted = self.head.data
                self.head = current.next_node
                current = None
                return deleted
            else:
                while id > 1 :
                    current = current.next_node
                    id -= 1
                deleted = current.next_node.data
                next = current.next_node.next_node
                current.next_node = None
                current.next_node = next
                return deleted

    def index(self, num):
        current = self.head
        counter = 0
        while(current != None):
            if current.data == num:
                return counter
            else:
                counter+=1
                current = current.next_node
        return -1
    




if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.append(15)   
    linkedlist.append(21)
    linkedlist.append(11)
    linkedlist.append(36)
    linkedlist.append(37)
    linkedlist.append(25)
    linkedlist.print()
    print(linkedlist.delete(3))
    print(linkedlist.delete(0))
    print(linkedlist.delete(8))
    print(linkedlist.delete(1))
    linkedlist.print()