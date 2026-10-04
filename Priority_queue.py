from bank_loan_application import BankLoanApplication
from priority_node import PriorityNode

class PriorityQueue():
    def __init__(self, next=None):
        self.rear_node = None
        self.front_node = None
        self.size = 0
        self.priority = 0.0

    def __str__(self):
        elements = ''
        prioritynode_ref = self.front_node
        while prioritynode_ref is not None: 
            elements = str(prioritynode_ref.data) + ' ' + elements 
            prioritynode_ref = prioritynode_ref.next 
        return elements 
   # application=BankLoanApplication()
    def priority_enqueue(self,application,priority):
        if not isinstance(application, BankLoanApplication):
            return False
        
        priority=application.priority
        new_prioritynode = PriorityNode(application,priority) 
        
       # self.size += 1 
       
        if self.rear_node is None: 
            self.rear_node = new_prioritynode 
            self.front_node = new_prioritynode 
            
        elif priority > self.rear_node.priority:
             new_prioritynode.next=self.rear_node
             self.rear_node=new_prioritynode
        else :
            current_node=self.rear_node
            while current_node.next is not None and current_node.next.priority >=priority:
                current_node=current_node.next
            new_prioritynode.next=current_node.next
            current_node.next=new_prioritynode
            
            if new_prioritynode.next is None:
                self.rear_node=new_prioritynode
                                
        self.size+=1
        
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            removed_node=self.front_node
            self.front_node=self.front_node.next
            
            self.size-=1
            
            return removed_node.data

    def get_front(self):
        if self.is_empty():
            return None
        return self.front_node.data
    #def rear(self):
     #   return self.rear_node.data
    #def size(self):
     #   return self.size
    def is_empty(self):
        return self.size==0

