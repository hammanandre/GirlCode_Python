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
            print ('omnomom!!')
        else:
            print (self.data['name']+' is not hungry!')
```

