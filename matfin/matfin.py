import math
class Capitalize:

    def __init__(self, interest = None, periods = None, 
                present_value = None, future_value = None):
        self.params = [interest,periods,present_value,future_value]
    
    def _check_params(self):
        try:
            list(map(float,self.params))
            return True
        except ValueError:
            raise ValueError('A non-number argument was given')
        except TypeError:
            none_count = sum(x is None for x in self.params)
            if none_count !=1:
                raise TypeError('There are missing arguments')
    
    def _frequency(self,ifreq,nfreq, r):
        if ifreq == 'M' and nfreq == 'Y':
            r = (1 + r)**(1/12) - 1
        if ifreq == 'Y' and nfreq == 'M':
            r = (1 + r)**(12) - 1
        elif ifreq == nfreq:
            pass
        else:
            raise ValueError('Invalid frequency')
        return r

    def simple(self):
        #fv = pv(1 + r*n)
        self._check_params()
        r, n, pv, fv = self.params[0], self.params[1], self.params[2], self.params[3]
        if r == None:
            result = (fv/pv - 1)/n
        elif n == None:
            result = (fv/pv - 1)/r
        elif pv == None:
            result = fv/(1 + r*n)
        elif fv == None:
            result = pv*(1 + r*n)
        else:
            raise TypeError('Capitalize.simple() takes 3 positional arguments but 4 were given')
        return result

    def compound(self,interest_freq = None, period_freq = None):
        #pv = fv/(1 + r)^n 
        self._check_params()
        r, n, pv, fv = self.params[0], self.params[1], self.params[2], self.params[3]
        #print(interest_freq, period_freq)
        r = self._frequency(interest_freq,period_freq,r)
        if r == None:
            result = (fv/pv - 1)/n
        elif n == None:
            result = (fv/pv - 1)/r
        elif pv == None:
            result = fv/((1 + r)**n)
        elif fv == None:
            result = pv*((1 + r)**n)
        else:
            raise TypeError('Capitalize.compound() takes 3 positional arguments but 4 were given')       
        return result

    def continuous(self, debug = False):
        result = None
        if debug:
            print('Capitalização Composta Contínua')
        return result
        
