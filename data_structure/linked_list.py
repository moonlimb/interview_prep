class Node:
    def __init__(self, init_data, next=None):
        self.data = init_data
        self.next = next

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

    def set_data(self,new_data):
        self.data = new_data
    
    def set_next(self, new_next):
        self.next = new_next
    
    def __repr__(self):
        return 'Node(%s)' %(self.data)

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def is_empty(self):
        return self.data == None
 
    def get_length(self):
        len_list = 0
        current_node = self.data
        while (self.head.data != None):
            len_list+=1
            current_node = self.next 
        return len_list 

    def push(self, data):
        pass

    def pop(self):
        last_node = self.data
        while (self.next):
            pass

    def pop(self, pos):
        pass

    def search(self, data):
        current_node = self.head
        found = False
        stop = False
        while current_node != None and not found and not stop:
            if current_node.get_data() == data:
                found = True 
            current_node = current_node.next
    "removes the node with matching data from the list; assume that the item is present in the list"         
    def remove(self, data):
        while (self.next):
           pass                                  

    def insert_after(self, element, data):
        pass

    def print_list(self):
        current_node = self.data
        while node:  
            print current_node.data
            current_node = node.next

    def __repr__(self):
        list_of_nodes= []
        node = self.head
        while node.next:
            list_of_nodes.append(Node(node.data)) 
        return ' '.join(list_of_nodes)

    def __str__(self):
        list_of_nodes = []
        node = self.head
        while node.next:
            list_of_nodes.append(node.data)
            node = node.next
        return ' '.join(list_of_nodes)  

