#Библиотека классов
#TODO: убрать и заменить на алфавиты

class Answer():
    response = None
    action = None
    target = None
    def __init__(self, r, a, target = None):
        self.response = r
        self.action = a
        self.target = target
    def Upd(self, response = None, action = None, target = None):
        if action != None:
            self.action = action
        if response != None:
            self.response = response
        if target != None:
            self.target = target
            
class Action():
    name = None
    function = None

    def __init__(self, name, func):
        self.name = name
        self.function = func







#END
#Code by Oria
