# Workshop 4
## Goals
In Workshop 4 we shall be looking at some more of the functionality in numpy as well as introducing the concept of Pandas.

We'll specifically look at indexing, reshaping and broadcasting of numpy arrays. Then look at some structured data arrays in numpy and then finally we'll be introduced to a pandas.


## Indexing 

Back in workshop 3 we looked at numpy arrays and spoke about how they are the same as normal python lists they are just limited to one data type though and cannot change due to the optimisations under the hood. 

With that context lets look at some cool indexing we can do with numpy.

```python
import numpy as np

x = np.arange(1,10)
print(x)
# [1 2 3 4 5 6 7 8 9]
```

ok now that we have a basic numpy array with some data in it again, remember that they are type locked. 
as you see there they are all ints. 

```python
x[0] = 3.14159 # this will be truncated 
print(x)
# [3 2 3 4 5 6 7 8 9]

x2 = np.linspace(1, 10, 10)
print(x2)
# [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
```
note the linspace function works diffrently and gives you 10 values evenly distributed between teh two ends. they are floats and as such does accept pi
```python
x2[0] = 3.14159 # this will not be truncated
print(x2)
#[ 3.14159  2.   3.   4.  5.   6.   7.  8.  9.  10. ]
```

With the indexing, we can single index, reverse index to get the value from the back od the array, list input index and them Mask indexes we did in workshop 3 refer to the end of that one for a refresher

```python
print(x)
#[3 2 3 4 5 6 7 8 9]

print(x[0])
#3 single index

print(x[-1])
#9 the reversed index (value from the back)

ind = [2,4,7]
print(x[ind])
#[3 5 8] a list of indexes returns their values
```

Now it's important to note with putting a numpy array index into the the array you get back values fromatted accourinding to what you put in. 

```python
ind = np.array([[4, 1],[1, 7]])
print(x[ind])
#[[5 2][2 8]]
```

## Array slicing 

So while the [] notation allows us to access the indexes we can combine that with the : syntax to slice us out some subarrays. 

What this sytax ends us looking like is

```python
x[start:stop:step]
```

If any of those are left out they default to start=0, stop=size of dimension, step=1.

So with that in mind a few quick examples look like this:

```python
x[:5]  # first five elements
#[0 1 2 3 4]

x[5:]  # elements after index 5
#[5 6 7 8 9]

x[4:7]  # middle sub-array
#[4 5 6]

x[::2]  # every other element
#[0 2 4 6 8]

```
Keep in mind the reversed index we spoke about just earlier, the same logic holds with the step, so if we make the step -1
```python
x[::-1]  # all elements  are now being reversed
#[9 8 7 6 5 4 3 2 1 0]
```


Working with subarrays and slicing there is an important thing to remember, 
we are not making copies of this data, it all still refers to the same data, it's like a view of the data, if you change it it will change the original. 

This is a very useful feature to allow us to consider slices of a large data set at a time. 


```python 
x = np.arange(12).reshape((3, 4))
print(x)
#[[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]]

x_sample = x[:2,:2]
print(x_sample)
#[[0 1]
# [4 5]]

x_sample[0,1] = 2
print(x_sample)
#[[0 2]
# [4 5]]


print(x)
#[[ 0  2  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]]
```

However sometimes you do want to have another copy of your data for some reason. In that case you could just let you subarray index sample know you are copying, you do that so:

```python 
x_copy = x[:2,:2].copy()
```


## Reshaping Arrays

In the last example of the subarray section we wanted an array with 3 rows and 4 colombs so we used reshape to do that. Reshape is a very versatile way to reshape arrays, but do note you want to keep the collection the same size as the reshaped array. 

Similar to the subarray/array slicing reshape recreates a no-copy "view" of your data, so it's very versatile and light. 

## [Broadcasting arrays](https://jakevdp.github.io/PythonDataScienceHandbook/06.00-figure-code.html#Broadcasting)

Broadcasting arrays basically refer to the use of these "views" that we spoke of earlier to perform the very fast numpy functionalities on a set of arrays of diffrent sizes. 


For this section we are gonna use a [cool script](https://jakevdp.github.io/PythonDataScienceHandbook/06.00-figure-code.html#Broadcasting) someone else made and we are gonna put it in a file and run it, it will use numpy and matplotlib to save us a diagram that show how broadcasting works. (Refer to diagram and explaination in video for this workshop.) 

So what can we use this for:
- a host of statistical and experiment data organinisation things. 
- remapping data base values
- plotting functions

I found a cool example of plotting a function [here](https://jakevdp.github.io/PythonDataScienceHandbook/04.04-density-and-contour-plots.html) if you want to check it out but I will do data visualisation in an upcoming workshop.

## Numpy's Structured Arrays

Numpy's structured arrays is a way to store Compound and heterogeneous data effeciently, the numpy docs mention ["Structured datatypes are designed to be able to mimic ‘structs’ in the C language, and share a similar memory layout. They are meant for interfacing with C code and for low-level manipulation of structured buffers"](https://numpy.org/doc/stable/user/basics.rec.html?highlight=structured%20array#module-numpy.doc.structured_arrays) as such Pandas are much closer matched to what we will be doing but I'll quickly run over structured arrays with a few example cases in these notes incase they help.

So lets go back to our creatures example, if we wanted a single object with all the data in it that wasn't a class but a highly effecient numpy object we'd have this data:

```python
name = ['Cat', 'mouse', 'Fluffy', 'Whiskers']
age = [5, 4, 11, 34]
weight = [12.0, 5.5, 23.0, 45.5]

x = np.zeros(4, dtype=int) # make a numpy array that's empty of type int


dataformat = {'names':('name', 'age', 'weight'), 'formats':('U10', 'i4', 'f8')}
# make empty numpy structrued array
data = np.zeros(4, dtype=dataformat)
print(data.dtype)

```

As you saw there our data type has some intresting formats in, those are just the shorthand for this and you can use the short hand as well instead of a string
```

'b'	Byte	                np.dtype('b')
'i'	Signed integer	        np.dtype('i4') == np.int32
'u'	Unsigned integer	    np.dtype('u1') == np.uint8
'f'	Floating point	        np.dtype('f8') == np.int64
'c'	Complex floating point	np.dtype('c16') == np.complex128
'U'	Unicode string	        np.dtype('U') == np.str_
'V'	Raw data (void)	        np.dtype('V') == np.void
```

Once we have the new numpy structured array we can just assign the data into it
```python
data['name'] = name
data['age'] = age
data['weight'] = weight
print(data)

# we can now interact with this object as you would normally
# it doesn't make much sense in this small example but it woul be very useful in large data sets

# Get all names
data['name']

# Get first row of data
data[0]

# Get the name from the last row
data[-1]['name']

# even the boolean masks we looked at last workshop works in here
# Get names where age is under 30
data[data['age'] < 30]['name']
```

## Onto Pandas

Pandas objects are basically a Numpy Structured array but instead of having numbers for rows and colomns we can be indexing on labels, making it much more human friendly.
Pandas also has a series of helper functions and tools and builtin features that just make everything a bit more human friendly.

We'll start off with two Pandas concepts, a Series and a Dataframe. 

A Pandas series is a one-dimensional array of data that has indexes. 


First lets make sure to import our pandas

```python 
import numpy as np
import pandas as pd

import numpy as np 
import pandas as pd 

data = pd.Series(np.arange(5))
print(data)
print(data.values)
print(data.index)
```

As you can see the pandas series sofar just looks like a normal array, but the magic comes in with you can replace the index with anything

```python 
data = pd.Series([0, 1, 2, 3],index=['a', 'b', 'c', 'd'])
print (data)

# you'd now index on your new index values to get the values
print (data['a'])
```

A Pandas Series is almost analagous to a Python Dictionary, in fact you can create a Series from a dictionary. 

```python 
population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
print(population)
```

Now if a Series is a Single Dimensional array then a DataFrame in Pandas is a multi-Dimensional array equivelant.
Lets add some more data into the mix and make a second series with the area and then put the two series into a DataFrame

```python 
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
print(area)

states = pd.DataFrame({'population': population,
                       'area': area})
print(states)
```
