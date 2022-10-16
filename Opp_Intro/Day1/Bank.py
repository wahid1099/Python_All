class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw =100
        self.max_withdraw=10000

    def get_balance(self):
        return self.balance
    
    def withdraw(self,ammount):
        if ammount<self.min_withdraw:
            return f'No money for you. Minimum withdraw: {self.min_withdraw}'
        elif ammount>self.max_withdraw:
                        return f'You have crossed the max limit. Maximum withdraw: {self.max_withdraw}'
        elif ammount>self.balance:
                        return 'You are broke!!! No money for you'
        else :
         self.balance = self.balance - ammount
         return f'Here is your money: {ammount}'
        
    def deposit(self, ammount):
        self.balance =self.balance +ammount


my_bank = Bank(8000)
reply = my_bank.withdraw(900)
print(reply)
print(my_bank.get_balance())
my_bank.deposit(5000)
print(my_bank.get_balance())

