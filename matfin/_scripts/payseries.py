import math

class PayementSeries:
    
    def __init__(self, payement = None, interest_rate = None, periods = None, present_amount = None, future_amount = None):
        self.payement = payement
        self.interest_rate = interest_rate
        self.periods = periods
        self.present_amount = present_amount
        self.future_amount = future_amount
        self.params = [payement,interest_rate,periods,present_amount,future_amount]
    #fv = pmt*(((1+i)**n -1)/i)
    #pv = fv*(1/(1+i)**n)
    #fv = pv/(1/(1+i)**n)
    #pmt = fv/(((1+i)**n -1)/i)
    #pmt = (pv/(1/(1+i)**n)) /  (((1+i)**n -1)/i)
    def post(self):
        pmt,i,n,pv,fv = self.params
        if fv == None:
            pass
            #fv = pmt*(((1+i)**n -1)/i)
            #pv = fv*(1/(1+i)**n)
            #return {'pv' : pv, 'fv': fv}
        elif pmt == None:
            if fv == None and pv != None:
                pmt = (pv/(1/(1+i)**n))/ (((1+i)**n -1)/i)
                return pmt
            elif fv != None:
                pmt = fv/(((1+i)**n -1)/i)
                return pmt
        elif pv == None:
            #fv = pmt*(((1+i)**n -1)/i)
            #pv = fv*(1/(1+i)**n)
            



    def ante(self):
        pass