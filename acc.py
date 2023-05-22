class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """"This class generates checking amount object"""

    type="checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee

ayo_checking=Checking("Account\\ayo.txt", 1)
ayo_checking.transfer(110)
print(ayo_checking.balance)
ayo_checking.commit()
print(ayo_checking.type)

martins_checking=Checking("Account\\martins.txt", 1)
martins_checking.transfer(120)
print(martins_checking.balance)
martins_checking.commit()
print(martins_checking.type)

print(martins_checking.__doc__)