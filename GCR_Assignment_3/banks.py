class Bank():
    deposit = 0

    def __init__(self):
        self.deposit = 0

    def getBalance(self):
        print(self.deposit)


class IndianBank(Bank):
    def __init__(self):
        self.deposit = 40000


class Cub(Bank):
    def __init__(self):
        self.deposit = 15000


class Hdfc(Bank):
    def __init__(self):
        self.deposit = 30000


bank = Bank()
ib = IndianBank()
cub = Cub()
hdfc = Hdfc()
bank.getBalance()
cub.getBalance()
ib.getBalance()
hdfc.getBalance()
