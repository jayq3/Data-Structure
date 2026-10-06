class Customer: 
     auto_id = 1 
     __slots__ = ('id', 'last_name', 'first_name', 'address', 'mobile_number')  
     def __init__(self, last_name, first_name, address, mobile_number): 
         self.id = Customer.auto_id 
         self.last_name = last_name 
         self.first_name = first_name 
         self.address = address 
         self.mobile_number = mobile_number 
         Customer.auto_increment() 
     @classmethod
     def auto_increment(cls): 
         cls.auto_id +=1 
if __name__=='__main__': 
    c1 = Customer('Hope', 'Bob', '#45 Wanstead Heights, St. James', '2456789') 
    print(f"Welcome {c1.first_name} {c1.last_name} (ID#{c1.id}).") 
    print(f"Your address is: {c1.address}.") 
    print(f"Your mobile telephone number is: {c1.mobile_number}.", end="\n\n") 

    c2 = Customer('Smith', 'Fred', '#88 Homstead, Christ Church', '2671111') 
    print(f"Welcome {c2.first_name} {c2.last_name} (ID#{c2.id}).") 
    print(f"Your address is: {c2.address}.") 
    print(f"Your mobile telephone number is: {c2.mobile_number}.", end="\n\n") 

    c3 = Customer('White', 'Terry', '#1 Grazettes Terrace, St. Michael', '2234547') 
    print(f"Welcome {c3.first_name} {c3.last_name} (ID#{c3.id}).") 
    print(f"Your address is: {c3.address}.") 
    print(f"Your mobile telephone number is: {c3.mobile_number}.", end="\n\n")