class Card:
    balance = 0

    # A constuctor is then created that initializes every new object added to the class
    def __init__(self,bal):
        self.balance = bal

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount + (0.2 *amount)
            return self.printReceipt(self.balance,amount)
        else:
            return "Insufficient Funds"

    def printReceipt(self,balance,withdraw):

        return """ AMOUNT............{}
                   BALANCE...........{}
        """.format(withdraw,balance)