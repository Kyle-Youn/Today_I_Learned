class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first + self.second
        return result
    
    def div(self):
        result = self.first + self.second
        return result
    

class MoreFourcal(Fourcal):
    def pow(self):
        result = self.first ** self.second
        return result
    

a = MoreFourcal(4, 2)

a.pow()
