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
    
    def _frequency_dicrete(self,ifreq,nfreq, r):
        if ifreq == nfreq:
            pass
        elif ifreq == 'M' and nfreq == 'Y':
            r = (1 + r)**(1/12) - 1
        elif ifreq == 'M' and nfreq == 'd':
            r = (1 + r)**(30) - 1
        elif ifreq == 'Y' and nfreq == 'M':
            r = (1 + r)**(12) - 1
        elif ifreq == 'Y' and nfreq == 'd':
            r = (1 + r)**365 - 1
        elif ifreq == 'd' and nfreq == 'M':
            r = (1 + r)**(1/30) - 1
        elif ifreq == 'd' and nfreq == 'Y':
            r = (1 + r)**(1/365) - 1
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
        r = self._frequency_dicrete(interest_freq,period_freq,r)
        if r == None:
            #fv = pv*(1+r)**n
            #(1+r)**n = fv/pv
            #(1+r) = (fv/pv)**(1/n)
            result = (fv/pv)**(1/n) - 1
        elif n == None:
            #   ln(fv) =  ln(pv * (1+r)**n)
            #   ln(fv) = ln(pv) + n*ln(1+r)
            #   n*lnl(1+r) = ln(fv/pv)
            #   n = ln(fv/pv)/ln(1 +r)
            result = (math.log(fv/pv))/(math.log(1 + r))
        elif pv == None:
            result = fv/(1 + r)**n
        elif fv == None:
            result = pv*((1+r)**n)
        else:
            raise TypeError('Capitalize.compound() takes 3 positional arguments but 4 were given')       
        return result

    def continuous(self, interest_freq = None, period_freq = None):
        # fv = pv*exp(r*t)
        e = math.exp(1)
        self._check_params()
        r, n, pv, fv = self.params[0], self.params[1], self.params[2], self.params[3]
        if r == None:
            result = math.log(fv/pv)/n
        elif n == None:
            #fv = pv*e**(r*n)
            #ln(fv)= ln(pv) + (r*n)ln(e)
            #(r*n) = ln(fv) - ln(pv)
            #n = ln(fv/pv)/r
            result = math.log(fv/pv)/r
        elif pv == None:
            result = fv/(e**(r*n))
        elif fv == None:
            result = pv*(e**(r*n))
        else:
            raise TypeError('Capitalize.compound() takes 3 positional arguments but 4 were given')       
        return result