class PayementSeries:
    
    def __init__(self, payement = None, interest_rate = None, periods = None, present_amount = None, future_amount = None):
        self.payement = payement
        self.interest_rate = interest_rate
        self.periods = periods
        self.present_amount = present_amount
        self.future_amount = future_amount