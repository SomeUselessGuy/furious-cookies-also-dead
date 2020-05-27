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
            

