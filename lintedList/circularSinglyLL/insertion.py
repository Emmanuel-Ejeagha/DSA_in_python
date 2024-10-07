# circular singly linked list

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    # Creation of circular singly linked list
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "the CSLL has been created"
    
    # Insert method in circular singly linked list
    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head referencenis None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next

myCircularSLL = CircularSLL()
myCircularSLL.createCSLL(1)

print([node.value for node in myCircularSLL])
