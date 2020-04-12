from Creature import Creature
from SaveState import Saver
from time import sleep
from os import system

class CreatureManager(Saver):
    data = []
    def __init__(self):
        self.load()
        print('------------------------------')
        print('Welcome to my creatures!')
        print('------------------------------')
    def show(self):
        print (self.data)
    def AddCreature(self):
        print("Let's add a new Creature!")
        NewPet = {}
        NewPet['name'] = input("What is the new pet called? ")
        NewPet['age'] = int(input("How old is the pet? "))
        NewPet['weight'] = int(input("What does the pet weigh? "))
        NewPet['hungry'] = True
        NewPet['photo'] = input("What does the pet look like? ")
        self.data.append(Creature(NewPet))
        #self.save(self.data)
    def FeedPets(self):
        for creature in self.data:
            creature.feed()



manager = CreatureManager()
QuitApp = True
while QuitApp:
    if input('Do you want to add a Pet? [Y/N]').upper() == "Y":
        manager.AddCreature()
    manager.FeedPets()
    sleep(2)
    system('cls')
    if input('Do you want to quit [Y/N]').upper() == "Y":
        QuitApp = False





#cat = Creature({'name': "Fluffy",'age': 3,'weight': 2.4,'hungry': True,'photo': "(=^O.O^=)_"})
#mouse = Creature({'name': 'Mouse','age': 6,'weight': 1.5,'hungry': False,'photo': '<:3 )~~~~'})

#cat.show()
#cat.feed()
#mouse.show()
#mouse.feed()

#StateSaver = Saver()
#StateSaver.save(mouse.data)
