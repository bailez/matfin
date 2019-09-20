import math
from .freq import FrequencyAjustment

class Interest:

    def __init__(self, rate = None, periods = None, 
                present_value = None, future_value = None):
    
        self.params = [rate,periods,present_value,future_value]
        try:
            list(map(float,self.params))
        except ValueError:
            raise ValueError('A non-number argument was given')
        except TypeError:
            nargs = 4 - sum(x is None for x in self.params)
            if nargs != 3:
                raise TypeError('Interest.simple() takes 3 positional arguments but {} were given'.format(nargs))

    def simple(self, interest_frequency=None, period_frequency=None):
        r, n, pv, fv = self.params[0], self.params[1], self.params[2], self.params[3]
        if r == None:
            n = FrequencyAjustment(period_frequency,interest_frequency,periods=n).simple()
            return (fv/pv - 1)/n
        else:
            r = FrequencyAjustment(interest_frequency,period_frequency,rate=r).simple()
            if n == None:
                return (fv/pv - 1)/r
            elif pv == None:
                return fv/(1 + r*n)
            elif fv == None:
                return pv*(1 + r*n)
            else:
                raise TypeError('Interest.simple() takes 3 positional arguments but 4 were given')

    def compound(self, interest_frequency=None, period_frequency=None):
        r, n, pv, fv = self.params[0], self.params[1], self.params[2], self.params[3]
        if r == None:
            n = FrequencyAjustment(period_frequency,interest_frequency,periods=n).compound()
            return (fv/pv)**(1/n) - 1
        else:
            r = FrequencyAjustment(interest_frequency,period_frequency,rate=r).compound()
            if n == None:
                return (math.log(fv/pv))/(math.log(1 + r))
            elif pv == None:
                return fv/(1 + r)**n
            elif fv == None:
                return pv*((1+r)**n)
            else:
                raise TypeError('Interest.compound() takes 3 positional arguments but 4 were given')

    def continuous(self, interest_frequency=None, period_frequency=None):
        e = math.exp(1)
        r, n, pv, fv = self.params[0], self.params[1], self.params[2], self.params[3]
        if r == None:
            n = FrequencyAjustment(period_frequency,interest_frequency,periods=n).continous()
            return math.log(fv/pv)/n
        else:
            r = FrequencyAjustment(interest_frequency,period_frequency,rate=r).continous()
            if n == None:
                return math.log(fv/pv)/r
            elif pv == None:
                return fv/(e**(r*n))
            elif fv == None:
                return pv*(e**(r*n))
            else:
                raise TypeError('Interest.compound() takes 3 positional arguments but 4 were given')