class FrequencyAjustment:

    def __init__(self, input_frequency, output_frequency, rate = None, periods = None):
        if input_frequency == None and output_frequency == None:
            input_frequency = 'Y'
            output_frequency = 'Y'

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
            if i not in self.time:
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
            return r/k
        elif r == None:
            return n*k