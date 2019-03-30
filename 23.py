

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:

    def __init__(self):
        self.head = None
    
    def printList(self): #traverse a linked list
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def removeDuplicates(self):  # remove duplicate method for sorted list
        temp = self.head 
        if temp is None: 
            return
        while temp.next is not None: 
            if temp.data == temp.next.data: 
                temp.next = None
                temp.next = temp.next.next 
            else: 
                temp = temp.next
        
     
    
    def removeDup(self):    # remove duplicate method for unsorted list
        
        elements = []
        
        temp = self.head #current node; starting at the head
        
        if temp.next is None:
            return
        while temp.next:
            if temp.data in elements:
               temp.next = None 
               temp.next = temp.next.next
            else:
                
                elements.append(temp.data)
        
                temp = temp.next

        return self
    
    def remove_dup_followup(self):
        
        current = self.head #current node; starting at the head
        
        if current.next == None:
            return
        
        while current.next:
            if current.data == current.next.data:
                
                current.next = current.next.next
                
            else:
                current = current.next
        
    def remove_middle(self):
        
        count = 0
        
        
        node = self.head
        
        
        
        while node:
            
            count += 1
            
            node = node.next
        locator = 0
        
        while node:
            
            locator += 1
            
            if locator == count//2:
                
                node = node.next.next
                
                print(node.data)
                
            else:
                
                node = node.next
                print(node.data)
            
        return self
         
            
        

llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(1)



llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

llist.remove_middle()
llist.printList()


        
        
    
