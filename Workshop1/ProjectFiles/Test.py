import json

creature_1 = {
    'name':"Fluffy",
    'age': 3,
    'weight':2.4,
    'hungry':True,
    'photo':"(=^o.o^=)_" #This is a string picture emoji
}
creature_2 = {
    'name':"Rat",
    'age': 1,
    'weight':1.4,
    'hungry':False,
    'photo':"<:3 )~~~~" #This is a string picture emoji
}

creatures = [creature_1,creature_2]

def feedCreature(ToFeed):
    if ToFeed['hungry'] == True:
        ToFeed['hungry'] = False
        ToFeed['weight'] = ToFeed['weight']+0.5
        print(ToFeed['name']+" has been fed")
    else:
        print(ToFeed['name'] + " was not hungry")
        ToFeed['hungry'] = True

def AddCreature():
    print("Lets add a creature")
    NewCreature = {}
    NewCreature['name'] = input("What do you want to call the creature? ")
    NewCreature['age'] = int(input("How old is the creature?"))
    NewCreature['weight'] = float(input("How heavy is the creature?"))
    NewCreature['hungry'] = True
    NewCreature['photo'] = input("How does the creature look?")
    creatures.append(NewCreature)

def save():
    file = open('creature.json','w')
    json.dump(creatures,file)
    file.close()
    print("Saved our changes to creatures")

def load():
    try:
        file = open('creature.json','r')
        global creatures
        creatures = json.load(file)
        print("Loaded saved Creatures")
    except FileNotFoundError:
        print("No saved creatures")


print ('------------------------------')
print ('Welcome to a tamagotchi code toy!')
print ('------------------------------')

load()

if input("Do you want to add a new creature? [Y/N]").upper() == "Y":
    AddCreature()

for creature in creatures:
    print('')
    print ('------------------------------')
    print ('Hello ' + creature['name'] + '!')
    print (creature['photo'])
    print ('Weight: ' + str(creature['weight']))
    feedCreature(creature)
    print ('Weight: ' + str(creature['weight']))
    print ('------------------------------')

save()