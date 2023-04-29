class Testing:

    compound = 0
    future = 0

    def evaluate(self):
        if (self.compound - 1) > 1:
            raise Exception()

    def calculate(self, capital = 0, period = 0, rate = 0):

        self.capital = capital
        self.period = period
        self.rate = rate
        self.compound = (1 + rate / 100) ** period
        self.future = self.compound * capital

        print(f'Considering capital = {self.capital}, period = {self.period} and rate = {self.rate} => result = {self.future}')

        try:
            self.evaluate()
        except Exception:
            print(f'Compound rate is over 100% = {int(self.compound * 100)}%')

try:
    var_capital = int(input('$ Capital? '))
    var_period = int(input('T Period?  '))
    var_rate = int(input('% Rate?    '))
    testing = Testing()
    testing.calculate(var_capital, var_period, var_rate)
except Exception:
    print('Invalid input values')


