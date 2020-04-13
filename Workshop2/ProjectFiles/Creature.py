class Creature:
    data = {}
    def __init__(self, data):
        self.data = data
    def show(self):
        print(self.data['photo'])
    def feed(self):
        if self.data['hungry'] == True:
            self.data['hungry'] = False
            self.data['weight'] = self.data['weight'] + 1
            print (self.data['name'] +' says omnomom!!')
        else:
            print (self.data['name']+' is not hungry!')

