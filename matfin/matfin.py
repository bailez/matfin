class Capitalize():
    def __init__(self, interest= None, payment= None, periods = None, present_value = None, future_value = None):
        self.r = interest
        self.p = payment
        self.n = periods
        self.pv = present_value
        self.fv = future_value

        pass
    
    def simple(self):
        print('Capitalização Simples')
    
    def compound(self):
        print('Capitalização Composta Discreta')

    def continuous(self):
        print('Capitalização Composta Contínua')
