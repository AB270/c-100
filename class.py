class bank(object):

    def __init__(self,cash_withdrawal,Balance_Enquiry):
        self.cash_withdrawal = cash_withdrawal
        self.Balance_Enquiry = Balance_Enquiry


    def start(self):
        print("Enter atm card...")

    def pin(self):
        print("pin")

    def transactionType(self):
        print("TransactionType")
        "Transaction related functionality here"
    
    def WithdrawalAmount(self,WithdrawalAmount):
        print("WithdrawalAmount")
        "Withdrawal Amount"


atm = bank(1000,28000)

print(atm)
