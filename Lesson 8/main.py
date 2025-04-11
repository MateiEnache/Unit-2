class BankAccount:
    __num_transactions = 0
    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.__balance = balance
    
    # getter method
    def get_balance(self):
        return f"${self.__balance:.2f}"

    def get_num_transactions(self):
        return BankAccount.__num_transactions
    
    # setter method

    def set_balance(self,amount):
        if amount>self.__balance:
            self.__balance = amount
            BankAccount.__num_transactions += 1
    
my_account = BankAccount("Matei",1234,50)
print(my_account.get_balance())
print(my_account.get_num_transactions())
my_account.set_balance(100)
print(my_account.get_balance())
print(my_account.get_num_transactions())