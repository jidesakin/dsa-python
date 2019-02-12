class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        current_position = 1
        current = self.head
        element = None
        
        
        while True:
            if current_position == position:
                element = current
                break
            else:
                current = current.next
                current_position = current_position + 1
        return element
    
    def insert(self, new_element, position):
        current_position = 1
        current = self.head
        while True:
            if current_position == position - 1:
                before_old_current = current
                old_current = current.next
                current = new_element
                before_old_current.next = current
                current.next = old_current
                break
            else:
                current = current.next
                current_position = current_position + 1

    
    def delete(self, value):
        current_position = 1
        current = self.head
        while True:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                    current = None
                    break
                else:
                    prev_element = self.get_position(current_position - 1)
                    next_element = self.get_position(current_position + 1)
                    prev_element.next = next_element
            else: 
                current = current.next
                current_position = current_position + 1

    def insert_first(self, new_element):
        current = self.head
        self.head = new_element
        self.head.next = current

    def delete_first(self):
        current = self.head
        if current:
            self.head = current.next

        return current

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)
        

    def pop(self):
        top = self.ll.delete_first()
        return top