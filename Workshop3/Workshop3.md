# Workshop 3
## Goals
Workshop 3 aims to take all the basics we covered in workshop 1 and workshop 2 and start applying them to some Data science applications. In this workshop we'll also cover numpy and matplot as some of the more task focused python libraries when it comes to datascience. 

The end goal of this workshop is to serve as an introduction to some of the expansion libraries to python as well as how they work. We'll also cover some performance debugging tools and talk about how to approach writing a application with performance in mind. 

## First steps 
- Install numpy 

    You install numpy using pip, pip is python's package manager. 
    ```
    pip install numpy
    ```
- Import numpy

    Numpy has a specific way of importing it that is regarded as standard

    ```python
    import numpy as np
    ```

## What is numpy

Numpy is a library(module) for python that is designed to handle Large multi-dimensional arrays and matrices as well as handling the execution of high-level math functions for these arrays.

The way numpy does this is by providing a series of universal functions (ufuncs) that calls optimised C compiled code in the back to operate on these data collections. 

Because pyhton is an interpreted language that has dynamic types it has alot of freedom, but this also means each variable has an overhead, as it has to store the type of data in the variable as well as the value in the variable. When iterating over a collection of data this becomes apparent in the speed of the execution, numpy solves this by providing many of the most common and useful arithmetic functions that are calls to optimised code in the back.

## Using Numpy

Lets do an example of the speed diffrence between default python and numpy. 

We want to calculate the reciprocals(1/x) of a list of random Ints, using both standard python as well as numpys notation and then we want to measure the diffrence in speed. 

To measure how long a function takes to execute we'll use TicToc a library that can calculate the time it took to do something. First we will install TicToc:

```python
pip install pytictoc
```

Then lets write our example.
We'll be using a vectorized operation that's provided by numpy, a vectorized operation refers to a statically types compiled routine provided by numpy. What this vectorized operation does is it moves the loop from within Python into the compiled layer and provides a function you can perform on an array that will then be applied to each element by precompiled satically typed code. This leads to a much faster execution time.

```python

import numpy as np
from pytictoc import TicToc
t = TicToc() #create instance of TicToc
np.random.seed(0) #Provide a seed to make the random numbers reproduceable

#a function to calculate the reciprocals of an array and return that array
def compute_reciprocals(values): 
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output

# using numpy create a numpy array of random ints between 1 and 100 that has 1000000 entries
values = np.random.randint(1, 100, size=1000000)

t.tic() #Start timer
processed_values = compute_reciprocals(values)
t.toc('The loop took: ') #Time elapsed since t.tic() with a return prefix
print(processed_values)


t.tic()
processed_values = 1.0 / values  # the vectorized operation
t.toc('The vectorized operation took: ')
print(processed_values)
```

These vectorized operations can not only be applied between numbers and arrays but also multiple arrays

The operator as seen there is a useful wrapper for a function inside of numpy, what this means is that the following is the exact same but with a diffrent syntax:

```python
processed_values = 1.0 / values
processed_values = np.divide(1,values)
```

numpy provides a selection of these operators:

```
+	    np.add()            Addition 
-	    np.subtract()       Subtraction 
-	    np.negative()       Negative
*	    np.multiply()       Multiplication 
**	    np.power()	        Exponentiation
/	    np.divide()	        Division 
%	    np.mod()            Remainder
//	    np.floor_divide()   Division Floor 
```

Numpy also provides a selection of useful trigonometric functions such as:

```
# provides a array of evenly spaced numbers over a specific interval
np.linspace(start,stop,num)

# machine precision values of trig functions
np.sin()
np.cos()
np.tan()

# You can provide there trig functions with an array and it will return a array of the values at those values
```

There are also aggregate functions in numpy: reduce and accumulate

Reduce applies a given operation to all the elecments of an array till only one value remains 

Accumulate stores all the intermediary values of the operation

You use these aggregators as such:

```python
# add is the operator and x is the array
np.add.reduce(x)
# this will add each value to the next in the array till only the total remains


# multiply is the operator and x is the array
np.multiply.accumulate(x)
# this will multiply each value and return an array of the intermediary values
```

## Using Data

Now lets use some real data and use some of what we have learned and learn about masking data.

Masking data refers to when you want to modify, count or otherwise perform an operation on data based on a specific criterion.

We are gonna use using some [data](https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/master/notebooks/data/Seattle2014.csv) from a diffrent course as it is publicly available.

This data is the rainfall statistics for Seattle in 2014.

First to extract what we want to be working with we'll use another companion package that is built ontop of numpy, that is pandas. We will be covering pandas in more depth next workshop, for now we'll just use some of its functionality to extract a NumPy array out of our data file.

```python 
pip install pandas
```

Now lets have pandas extract the numpy array for us:

```python
import numpy as np
import pandas as pd

# using pandas extract the rainfall in inches as a NumPy array from the file
rainfall = pd.read_csv('Seattle2014.csv')['PRCP'].values
millimeters = rainfall / 10  # 1/10mm -> mm
print(millimeters.shape)
```

millimeters.shape shows us there is 365 entries, one for each day in out array.

Lets display this data in a graph, for that we'll use another package called matplotlib to plot our graph. We'll go into detail about matplotlib next workshop

```
pip install matplotlib
pip install seaborn
```

Now lets use matplotlib to plot our data

```python
import matplotlib.pyplot as plt
import seaborn; seaborn.set()  # set plot styles
...
plt.hist(millimeters, 40)
plt.show()
```

Using the summery keyword in numpy we can calculate some statisics on this data:

```python
print("Number days without rain:      ", np.sum(millimeters == 0))
print("Number days with rain:         ", np.sum(millimeters != 0))
print("Days with more than 5 mm :", np.sum(millimeters > 5))
print("Rainy days with < 5 mm  :", np.sum((millimeters > 0) &
                                                (millimeters < 5)))
```
