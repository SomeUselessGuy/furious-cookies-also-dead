class Answer():
    response = None
    action = None
    target = None
    def New(self, r, a, target = None):
        self.response = r
        self.action = a
        self.target = target
        return self
    def Upd(self, response = None, action = None, target = None):
        if action != None:
            self.action = action
        if response != None:
            self.response = response
        if target != None:
            self.target = target
            
class Cl_Action():
    name = None
    function = None

    def N(self, func, name):
        self.name = name
        self.function = func
        return self

def Action(name, func): #Я не знаю как сделать мгновенную иницализацию.
                        #TODO: Сделать так, как делают все нормальные люди
    return Cl_Action().N(func, name)









#END
#Code by Oria
