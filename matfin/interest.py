import math

class Interest:

    def __init__(self, rate = None, periods = None, 
                present_value = None, future_value = None):
        self.params = [rate,periods,present_value,future_value]
    
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
    
    def simple(self):
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

    def compound(self):
        self._check_params()
        r, n, pv, fv = self.params[0], self.params[1], self.params[2], self.params[3]
        
        if r == None:
            result = (fv/pv)**(1/n) - 1
        elif n == None:
            result = (math.log(fv/pv))/(math.log(1 + r))
        elif pv == None:
            result = fv/(1 + r)**n
        elif fv == None:
            result = pv*((1+r)**n)
        else:
            raise TypeError('Capitalize.compound() takes 3 positional arguments but 4 were given')       
        return result

    def continuous(self):
        e = math.exp(1)
        self._check_params()
        r, n, pv, fv = self.params[0], self.params[1], self.params[2], self.params[3]
        if r == None:
            result = math.log(fv/pv)/n
        elif n == None:
            result = math.log(fv/pv)/r
        elif pv == None:
            result = fv/(e**(r*n))
        elif fv == None:
            result = pv*(e**(r*n))
        else:
            raise TypeError('Capitalize.compound() takes 3 positional arguments but 4 were given')       
        return result

class FrequencyAjustment:

    def __init__(self, rate_frequency, period_frequency):
        self.r_freq = rate_frequency
        self.p_freq = period_frequency