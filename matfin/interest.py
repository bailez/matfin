import math

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
            if nargs !=1:
                raise TypeError('Capitalize.simple() takes 3 positional arguments but {} were given'.format(nargs))
    
    def simple(self):
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

    def __init__(self, input_frequency, output_frequency, rate = None, periods = None):
        self.input_frequecy = input_frequency
        self.output_frequency = output_frequency
        self.rate = rate
        self.periods = periods
        
        if rate == None and periods == None:
            raise TypeError('FrequencyAjustment needs either rate or periods values')
        else:    
            try:
                list(map(float,[rate,periods]))
            except ValueError:
                raise ValueError('A non-number argument was given')
            except TypeError:
                pass

        ms = 0.001; s = ms*1000; m = s*60; h = m*60; d = h*24
        W = d*7; M = d*30 + 10*h; B = M*2; Q = M*3; S = M*6
        Y = d*365; D = Y*10; C = Y*100; X = Y*1000

        self.time = {
            'ms': ms, 's' : s,
            'm' : m, 'h' : h,
            'd' : d, 'W' : W,
            'M' : M, 'B' : B,
            'Q' : Q, 'S' : S,
            'Y' : Y, 'D' : D,
            'C' : C, 'X' : X
        }

        for i in [input_frequency, output_frequency]:
            if i in self.time:
                pass
            else:
                raise TypeError('The frequency {} given is not valid'.format(i))

    def simple(self):
        ifreq = self.time.get(self.input_frequecy)
        ofreq = self.time.get(self.output_frequency)
        r = self.rate; n = self.periods
        k = ifreq/ofreq
        if n == None:
            return r/k
        elif r == None:
            return n*k
    
    def compound(self):
        ifreq = self.time.get(self.input_frequecy)
        ofreq = self.time.get(self.output_frequency)
        r = self.rate; n = self.periods
        k = ifreq/ofreq
        if n == None:
            return ((1+r)**(1/k) - 1)
        elif r == None:
            return n*k
    
    def continous(self):
        ifreq = self.time.get(self.input_frequecy)
        ofreq = self.time.get(self.output_frequency)
        r = self.rate; n = self.periods
        k = ifreq/ofreq
        if n == None:
            return r*k
        elif r == None:
            return n*k