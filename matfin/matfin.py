class Capitalize:

    def __init__(self, interest = None, periods = None, 
                present_value = None, future_value = None):
        
        self.params = [interest,periods,present_value,future_value]
    
    def _check_params(self):
        pass

    def simple(self, debug=False):
        # S = P(1 + i * n)
        result = None
        r, n, pv, fv = self.params[0], self.params[1], self.params[2], self.params[3]
        if r == None:
            pass
        elif n == None:
            pass
        elif pv == None:
            pass
        elif fv == None:
            pass
        else:
            if debug:
                print('')
        if debug:
            print('Capitalização Simples')
        return result
    
    def compound(self, debug = False):
        result = None


        if debug:
            print('Capitalização Composta Discreta')
        return result
        

    def continuous(self, debug = False):
        result = None


        if debug:
            print('Capitalização Composta Contínua')
        return result
        
