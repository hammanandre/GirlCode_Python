import json 
from Creature import Creature

class Saver:
    def save(self,data):
        fp = open('save.json','w')
        json.dump(data,fp)
        print('Saved Data')
    def load(self):
        try:
            fp = open('save.json', 'r') 
            self.data = json.load(fp)
            tempcreatures = []
            for creaturedictionary in self.data:
                tempcreatures.append(Creature(creaturedictionary))
            self.data = tempcreatures
            print ('Loaded your saved data')
        except FileNotFoundError:
            print('No save files exist created new data')
            self.data = [{'name': "Fluffy",'age': 3,'weight': 2.4,'hungry': True,'photo': "(=^O.O^=)_"}]
