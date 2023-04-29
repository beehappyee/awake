class Client:

    def __init__(self, name='', amount=0):
        self.name = name
        self.amount = amount

    def disclose(self):
        return print(f'Client with name = {self.name} and amount = {self.amount}')

    def deposit(self, amount):
        if (amount >= 0):
            self.amount = self.amount + amount

    def withdrawal(self, amount):
        if (amount >= 0):
            self.amount = self.amount - amount

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        if (amount >= 0):
            self.amount = amount

client = Client('Juanito', 1000)

client.disclose()
client.setAmount(5000)
client.disclose()
client.setAmount(-10)
client.disclose()
client.deposit(500)
client.disclose()
client.deposit(-500)
client.disclose()
client.withdrawal(800)
client.disclose()
client.withdrawal(-800)
client.disclose()
