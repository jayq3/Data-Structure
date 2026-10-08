#from priority_queue import PriorityQueue\
    
class BankLoanApplication: 
    auto_id = 101

    __slots__ = ('id','customer_id','loan_amount', 'payment_period', 'interest_rate', 'priority')
    

    def __init__(self, customer_id, loan_amount, payment_period, interest_rate, priority): 
        self.id = BankLoanApplication.auto_id 
        self.customer_id = customer_id
        self.loan_amount = loan_amount 
        self.payment_period = payment_period 
        self.interest_rate = interest_rate 
        self.priority = priority 
        BankLoanApplication.auto_increment() 

    @classmethod
    def auto_increment(cls): 
        cls.auto_id +=1 
         
    def is_successful(self):
        return self.loan_amount<=15000
     
    def __str__(self):
        return(
            f"Application ID :{self.id}, "
            f"Customer ID : {self.customer_id}, "
            f"Loan Amount: {self.loan_amount}, "
            f"Payment Period: {self.payment_period}, "
            f"Interest Rate: {self.interest_rate}, "
            f"Priority : {self.priority}"
        )