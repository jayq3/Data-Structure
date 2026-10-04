from node import Node

class PriorityNode(Node):
    def __init__(self, data, priority, next=None): 
        super().__init__(data, next)
        #self.data = data 
        self.priority=priority 
        #self.next = next 
    def __str__(self):
        return f"{self.data}, {self.priority}, {self.next}"
   # if __name__ == '__main__': 
        #my_node = Node (5, None) 
        #print (f"Data = {my_node.data}, Next = {my_node.next}") 
        # optional parameters 
       # new_node = Node (10) 
        #print (f"Data = {new_node.data}, Next = {new_node.next}")