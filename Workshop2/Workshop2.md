# Workshop 2
## Goals
The workshop hopes to serve as an introduction to the basics of Classes and Modules in Python. We'll cover how to create classes and modules and use them to recreate the tamagotchi code toy we created in the previous workshop. 

The end product of this workshop will be a recreated version of last workshops code toy but using modular code that can be reused. 

## A Creature
- Create a new file called creature.py

To define a class we'll need a new keyword, the keyword class is gonna be used here. A class is a collection of data as well as functionality, similar to how a dictionary is a collection of data a class is a collection of both data and functionality. 

```python
class Creature:
    data = {}
```

A class is a form of a user defined type. Types like strings, ints and dictionary we have already used define what the data inside of a variable looks like. 

So with a class you can create your own data type with attached functionality.

When you create a class you create a data template, you have to create an instance of this template to use this type you've created. To create a new instance you call the function name as a method 

```pyhton
newcre = Creature() 
```

The variable newcre now contains an instance of the class Creature. 

When you create an instance of a class you can have some functionality happen during the create. This is called the Constructor. To define a constructor in Python you use a special function name: \_\_init__.

 To define a new function that takes a value in and assigns it into the internal data variable inside of a class you would do it like so:

 ```python
class Creature:
    data = {}
    def __init__(self, data):
        self.data = data
```

The paramater self inside of the constructor function is an aspect of all of the functions you'll define inside of a class. These paramaters self is filled in by python for you, you do not have to supply it, self refers to the instance of the class the function was called on. 

Thus to use this new constructor to fill in the data value inside of the class would look like this:

 ```python
class Creature:
    data = {}
    def __init__(self, data):
        self.data = data

newcre = Creature({'name': "Fluffy",'age': 3,'weight': 2.4,'hungry': True,'photo': "(=^O.O^=)_"})
```

Now that we've seen how to use the self variable lets recreate some more of the behaviour from our previous Tamagochi code toy. Making our creature.py look like this:

 ```python
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
```

Now we have a Creature that has the same behaviours as we had before. We can feed it and it will show a 'picture' of itself in the console. 

## A Manager

Lets use this creature class as a module and create a manager class to handle these creatures for us. 

A module in Python is basically loading a Python script and all the data and classes inside of it into another file to be used there. To do this we'll need the import keyword.

Create a new file called Main.py and and import our new Creature class into.

```python
import Creature

newcre = Creature.Creature({'name': "Fluffy",'age': 3,'weight': 2.4,'hungry': True,'photo': "(=^O.O^=)_"})
```

As you can see because the Class creature exists inside of file creature we have to refer to the File we imported from as well as then the Class inside of the file. The solution to this to make reffering to the class is the from keyword. 

```python
from Creature import Creature

newcre = Creature({'name': "Fluffy",'age': 3,'weight': 2.4,'hungry': True,'photo': "(=^O.O^=)_"})
```

Now we can refer to the Class only with our imported values. 

Using what we have learned lets create a new Class to manage our multiple creatures for us. We'll use a list inside of this Class that holds multiple creature class instances

```python
class CreatureManager():
    data = []
    def __init__(self):
        print('------------------------------')
        print('Welcome to my creatures!')
        print('------------------------------')
        self.show()
    def show(self):
        print (self.data)
        for creature in self.data:
            print(creature.data)
    def AddCreature(self):
        print("Let's add a new Creature!")
        NewPet = {}
        NewPet['name'] = input("What is the new pet called? ")
        NewPet['age'] = int(input("How old is the pet? "))
        NewPet['weight'] = int(input("What does the pet weigh? "))
        NewPet['hungry'] = True
        NewPet['photo'] = input("What does the pet look like? ")
        self.data.append(Creature(NewPet))
        self.show()
    def FeedPets(self):
        self.show()
        for creature in self.data:
            creature.feed()
```

Now we have a class that uses the add creature code to add a new creature from the first workshop adapted to work inside of a class, look at the usage of self there to add the creature class to the List inside of the CreatureManager class. 

This class also Shows an introductory message when it's first created as well as has a feed function that uses the feed function inside of each creature class to feed each creature. 

The show function in this classis completely for our debug so we can see inside of the class and what our data looks like. When the Show function is called it outputs something like this:

```python
[<Creature.Creature object at 0x0395F7D8>, <Creature.Creature object at 0x037F72E0>]
{'name': 'Mouse', 'age': 6, 'weight': 1.5, 'hungry': False, 'photo': '<:3 )~~~~'}
{'name': 'Cat', 'age': 2, 'weight': 25, 'hungry': True, 'photo': '(=^O.O^=)_'}
```

The first line show there are two creature objects in the list, that means two instances of our creature classes inside of the list and then the for loop in the show function shows us what the data inside of those classes looks like. The last two lines are the values inside of the dictionaries we are used to seeing. 

Now we have all the classes we need to have creatures as well as a manager for them, lets use them. 

```python
manager = CreatureManager()
if input('Do you want to add a Pet? [Y/N]').upper() == "Y":
        manager.AddCreature()
    manager.FeedPets()
```

When you run that code it shows the greeting line and then asks you if you want to add a creature, if you say yes it runs you through the add code we've had before and then it feeds all the creatures in our List in the manager. 

But it does this only once, lets have this happen repeatedly and only stop when the user says they are done. 

```python
QuitApp = True
while QuitApp:
    if input('Do you want to add a Pet? [Y/N]').upper() == "Y":
        manager.AddCreature()
    manager.FeedPets()
    if input('Do you want to quit [Y/N]').upper() == "Y":
        QuitApp = False
```

Now the code toy will ask the user if they are done and then stop running if they say yes. 

But it happens all immediatly after each other. Lets add a small wait into the program. For that we'll need to import another function from the built in time module. 

```python
from time import sleep
```

Then when we want to have the program wait we simply call this function, with a paramater of how long we want to wait in seconds

```python
sleep(2)
```
## Saving Data

Now we have the application running and waiting and closing, but it still uses only the data it gets during its runtime. Lets add the save code we had before into our code toy as a new Module and class. In a new file SaveState.py we first import our built in json module and then we will also need our creature module so that this new module knows how to deal with the creature class we created. 

```python
import json 
from Creature import Creature
class Saver:
    def save(self):
        fp = open('save.json','w')
        json.dump(self.data,fp)
        print('Saved Data')
    def load(self):
        fp = open('save.json', 'r') 
        self.data = json.load(fp)
        print ('Loaded your saved data')
```

This is our save load data we had last workshop converted abit to work with a class structre. But this will not save or load our data correctly as have a list of a custom class (Creature) in our CreatureManager class and the json module we imported only knows how to deal with built in python data types not user defined types like our class, so lets add some code to the save and load that will create a temporary variable that is a dictionary of the data we have to save and load respectively. 

```python
class Saver:
    def save(self):
        fp = open('save.json','w')
        creatureSaveData = []
        for creature in self.data:
            creatureSaveData.append(creature.data)
        json.dump(creatureSaveData,fp)
        print('Saved Data')
    def load(self):
        fp = open('save.json', 'r') 
        self.data = json.load(fp)
        tempcreatures = []
        for creaturedictionary in self.data:
            tempcreatures.append(Creature(creaturedictionary))
        self.data = tempcreatures
        print ('Loaded your saved data')
```

Now we have a class that will save and load the data by using a temporary variable to store the dictionary as well as create a new instance of the Creature class when it loads and add it to the data varaible inside of the class. But it will error out when trying to load the data and there isn't a save file already. So lets add a check if file doesn't exist create a new default data for the program to use. 

```python
class Saver:
    def save(self):
        fp = open('save.json','w')
        creatureSaveData = []
        for creature in self.data:
            creatureSaveData.append(creature.data)
        json.dump(creatureSaveData,fp)
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
            self.data = [Creature({'name': "Fluffy",'age': 3,'weight': 2.4,'hungry': True,'photo': "(=^O.O^=)_"})]

```
Now the Load code will either load a file or load a default object into the program if no file exists.

## Inheriting

But this class is seperate class that isn't connected to anything. 

The way we are gonna use this class is by inheriting the Saver class in our CreatureManager class, inheritance works by making all the data and functions in one class available to another class. So this effectively means you can use self.save in another class that inherits from the saver class, that's exactly what we want to do. 

The notation for inheriting looks like so:

```python

class Classname(ToInheritFrom):
```

so using that we change our creature manager to load on the creating of the class and save when we add a new creature, this looks like so:

```python
class CreatureManager(Saver):
    data = []
    def __init__(self):
        self.load()
        ...
    def AddCreature(self):
        ....
        self.save()
    def FeedPets(self):
        ...
        self.save()
```

I've replaced the code we already have here with ... to save on space, 
but here you can see we want to load the data when we create our manager and then keep saving the data whenever we changed anything in the data.

The self.show() function we call in all our functions will show us the data nicely. 

## Cleanup

Lets add one final bit of code just to clear the terminal whenever we post a bunch of things so that the console is nice and clear. For that we'll import the system function from os and class 'cls' which is the windows code to clear the console, that looks like so:

```python
from os import system

# then when we want to clear the console
system('cls')
```

# Erratum

During my workshop I gave on the video there was a problem with the load and saving of data that I got stuck on for a while and ended up saying I will cover in my notes. 

- What happened:

In my version of the loading of default data I had:
```python
 except FileNotFoundError:
    print('No save files exist created new data')
    self.data = [{'name': "Fluffy",'age': 3,'weight': 2.4,'hungry': True,'photo': "(=^O.O^=)_"}]
```

What this would do is it would set my data variable that is supposed to be full of instances of the Creature class equal to a list of adictionary of the data that is supposed to be inside of the Creature instance. So this would not work as the Creature class has extra functionality that does not exist in the dictionary alone. 

- The fix:
```python
 except FileNotFoundError:
    print('No save files exist created new data')
    self.data = [Creature({'name': "Fluffy",'age': 3,'weight': 2.4,'hungry': True,'photo': "(=^O.O^=)_"})]
```

When you change the Dictioarny in the list to be a Instance of Creature then all the code behaves as expected as the Code then recieves what it is expecting not a dictionary of data but an instance of Creature with that data in it. 

- How I Debugged:

I changed my Show() function in CreatureManager to show both the self.data as well as iterate through the data in the list and then it was instantly clear that I was having the wrong data inside of the List and that my wrong data was happening when I was loading, so I looked at my load function and saw the default data would not return a list of Creature of objects but actually a list with a dictionary inside of it, so updating the code to return the right type of data cleared up the problem. 
