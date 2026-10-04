from node import Node 

class LinkedList: 
   """Create a Singly Linked List""" 
   def __init__(self): 
      self.head = None 
      self.list_length=0
   def __str__(self): 
      list_items = " "
      node_ref=self.head
      while node_ref:
         list_items += f"{node_ref.data.first_name} {node_ref.data.last_name} {node_ref.data.id} {node_ref.data.mobile_number}"
         node_ref=node_ref.next
      return list_items  
   def search(self, key): 
      node_ref = self.head 
      customer_record =" "
      found = False 
      while node_ref: 
         if node_ref.data.last_name == key: 
            found = True 
            customer_record=f"{node_ref.data.first_name} {node_ref.data.last_name} {node_ref.data.id} {node_ref.data.address} {node_ref.data.mobile_number}"
            break 
         else:
            node_ref = node_ref.next 
      return node_ref  
      return customer_record
   
   def delete(self, key):
      deleted = False 
      current_node=self.head
      previous_node=None
      while current_node:
         if current_node.data==key:
            if not previous_node:
               self.head=current_node.next
            else:
               previous_node_ref.next=current_node.next
               delete=True
               self.list_length-=1
               break
         else:
            previous_node_ref=current_node
            current_node=current_node.next
      return deleted 
   
   def insert(self, record): 
      # Insert data into a sorted list (ascending order). 
      length=self.list_length
      new_node = Node(record) 
      self.list_length+=1  
      if self.head == None: 
          # if the list is empty simply insert the node 
          self.head = new_node 
      elif record.last_name < self.head.data.last_name: 
          # insert key at head of list 
          new_node.next = self.head 
          self.head = new_node 
      else: 
          # find the position to insert the new node at and insert it 
          current_node = self.head.next 
          previous_node = self.head 
          inserted = False 
          while current_node: 
             if record.last_name < current_node.data.last_name: 
                new_node.next = previous_node.next 
                previous_node.next = new_node 
                inserted = True 
             else: 
                previous_node = current_node 
                current_node = current_node.next 
                # if the key value is greater than the last list item, insert at end 
                if not inserted:
                   previous_node.next = new_node 
        
   def length(self): 
      return self.list_length
   