class loan_transaction():
     def __init__(self, customer_id, account_type, transaction,monthly_payment, interest_rate): 
             self.id = BankLoanApplication.auto_id 
             self.customer_id = customer_id
             self.account_type = account_type 
             self.transaction = transaction
             self.monthly_payment = monthly_payment 
             self.interest_rate = interest_rate 