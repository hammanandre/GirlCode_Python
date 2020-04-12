# Workshop 1
## Goals
The workshop hopes to serve as an introduction to the basics of Python in a beginner friendly fashion that illustrates how to create the basic data structures available in Python as well as how to interact with them. This workshop also shows how to save these data structures to a local file and interact with a Python application using command line commands. 


The end product of this workshop is a basic code toy similar to a tamagotchi program.


The “player” will have a “virtual creature” expressed in data that is saved to a local file and they can type basic commands to the application to interact with these data structures and generates a result that in turn gets updated in the local storage file.

- Setup a basic Python 3.X environment 
- Write a Hello World 
- Write a Tamagotchi Application
## First steps 
1. [Download](https://www.python.org/downloads/) the latest version of Python 3.X 
2. Install python making sure to tick the Add to Path option.
3. Make a new file called helloworld.py 
```python
print("Hello world!")
```
4. In a console in the same folder as the file run the file by typing.

\>Python .\helloworld.py 

If you recieve a Hello world! message in the console your setup is correct and everything is functional.

## A Creature
- Create a new file called creature.py

To build a creature we'll have to have some values that describe the attributes of the creature. 
Some of the basic values we'll use are intagers that are whole numbers,

floats that are fractions,

strings that is a set of characters

and Booleans that are a binary true or false value.


A variable in Python is defined by defining the variable name then a "=" and the value.

Variables in Python are not limited to a specific type, you can change the type of value inside of a variable by simply overriding it the same way you define a variable. 

A basic creature would be defined as:

```python
name = 'Fluffy'
age = 5
weight = 9.5
hungry = True
photo = '(=^o.o^=)__'
```

As variables contain a value, you can use those values by simply referring to the name of the variable like so.
```python
print(name + "says hi!")
print(photo)
```

Try run your new script the same way you ran your helloworld.py script but referring to the new file. 

A dictionary is another variable type that can hold a selection of diffrent variables and effectively group them as one object.
Variables defined inside a dictionary uses colons instead of equals signs to define their values. 

```python
creature = {
  'name': 'Fluffy',
  'hungry': True,
  'weight': 9.5,
  'age': 5,
  'photo': '(=^o.o^=)_',
}
```

Similarly accessing the values inside of Dictionary you have to specifically refer to the dictionary itself when getting the value of the variable. 

```python
print(creature['name'] + "says hi!")
print(creature['photo'])
print(creature)
```

We can also prepackage behaviours as functions. You define functions using the def key word.
After the keyword and inside the () sytax you can define a local variable that allows you to pass variables into the function. 
```python
def feed(cre):
    cre['hungry'] = False
    cre['weight'] = cre['weight'] + 0.5
    
print(creature)
feed(creature)
print(creature)
```

We now have a basic Tamagotchi:
```python
creature = {
  'name': 'Fluffy',
  'hungry': True,
  'weight': 9.5,
  'age': 5,
  'photo': '(=^o.o^=)_',
}

def feed(cre):
    cre['hungry'] = False
    cre['weight'] = cre['weight'] + 0.5
    
print(creature['name'] + "says hi!")
print(creature)
feed(creature)
print(creature)
```

Let's make it abit smarter by introducing some logic into what our creature can do. 
One of the most basic logic components is to compare things. 
In python we can use a check if a specific condition is met and then do something if it is or not. 

The syntax for this comparison looks like this:
```python
def feed(cre):
  if cre['hungry'] == True:
    cre['hungry'] = False
    cre['weight'] = cre['weight'] + 0.5
  else:
    print ('The creature is not hungry!')
    cre['weight'] = cre['weight'] + 0.5
    
```

The syntax is very similar to the def keywords just with diffrent keywords and without the () for a local variable.

Another type of collection variable like what the Dictionary does is a list, but where a Dictionary can contain a selection of diffrent variables and their values a list contains a selection of values at diffrent indexes. 

A List is define with the syntax:

Name = [var1,var2]

A useful way to go through the values in a List is using one of the Loops in Pyhton, a For loop does the same thing for every instance of something in a collection. 

The syntax for a For loop is:

for localvarName in Collection:


Applying these new concepts to our creature we end up with:
```python
creature_1 = {
  'name': 'Fluffy',
  'hungry': True,
  'weight': 9.5,
  'age': 5,
  'photo': '(=^o.o^=)_',
}

creature_2 = {
    'name': 'Rat',
    'age': 6,
    'weight': 1.5,
    'hungry': False,
    'photo': '<:3 )~~~~',
}

creatures = [creature_1, creature_2]

def feed(creature):
  if creature['hungry'] == True:
    creature['hungry'] = False
    creature['weight'] = creature['weight'] + 0.5
  else:
    print ('The creature is not hungry!')
    creature['weight'] = creature['weight'] + 1

for creature in creatures:
    print ('------------------------------')
    print ('Hello ' + creature['name'] + '!')
    print (creature['photo'])
    print ('Weight: ' + str(creature['weight']))
    feed(creature)
    print ('Weight: ' + str(creature['weight']))
    print ('------------------------------')    
```
## Interaction

Now that we have a creature or two lets start adding some interactions with our creatures. 

Python has a function that lets you provide a prompt and then return to you a string to use.

The syntax for this is:

```python
var = input("prompt")
```

We can also convert variables from one type to another, say we have a string (a collection of characters) to an intager (a whole number) the all we do is use pythons built in conversion functions. 

The syntax for this is:

```python
int(stringvar)
float(stringvar)
```

Most of Pythons built in data types also have functions attached to them. 

For example a string can be made all uppercase by adding a .upper() after and you can add a value to a list with an .append(var) descriptions and more examples can be found in the [Python docs](https://docs.python.org/3.8/library/index.html)

Baring these options in mind we can make a function that adds values to our creature options

```python
def AddCreature():
    print("Let's add a new pycreature!")
    NewCreature = {}
    NewCreature['name'] = input("What is the new creature called? ")
    NewCreature['age'] = int(input("How old is the creature? "))
    NewCreature['weight'] = float(input("What does the creature weigh? "))
    NewCreature['hungry'] = True
    NewCreature['photo'] = input("What does the creature look like? ")
    creatures.append(NewCreature)
```

And we make this happen optionally using more of these new concepts:

```python
if input("Do you want to add a new Creature? [Y/N]").upper() == "Y" :
    AddCreature()
```
