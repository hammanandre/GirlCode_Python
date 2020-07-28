# Workshop 6
## Goals
Workshop 6 is about programming a GUI.

We'll be using Tkinter for this purpose,
the previous libraries we've used sofar have plugins for this framework.

We'll go over how to display Pandas data as well as MatPlotLib figures in Tkinter.

## Into to Tkinter

Tkinter is a GUI Library that you can in code define what the library should draw and then it draws the relevant components in a window container.

To define the most basic window you would import Tkinter and define the window 

```python 
from tkinter import *

window = Tk()

window.mainloop()
#you call the window's mainloop which makes the window update and display
```

Now that we have a window we can start modifying the window and adding some content to this window.

Lets give the window a Title and define its size and shape as well as add some text in it.

````python 
from tkinter import *

window = Tk()

window.title("Welcome to MyUI app")
window.geometry('850x600')

lbl1 = Label(window, text= 'The Test Data')
lbl1.pack()

window.mainloop()
````

Here we are using one of the functions in Tkinter to draw a Label, 

There is a variety of functions inside of Tkinter that allows us to draw a range of GUI components.

These functions work similar to the MatPlotLib functions where you define the content and then call a draw on it.

In the case of the Label we define the Label and then store it in the variable lbl1, we then display it by calling .pack().

Tkinter has multiple options to display, a packing format and a grid layout option are some of the most common.

For now we will use the pack option.

To do interactions all we have to do is define some buttons and link functions to them.

Lets Define a label and a entry field with a button that prints the input string to our console.

````python 
from tkinter import *

window = Tk()

window.title("Welcome to MyUI app")
window.geometry('850x600')

lbl1 = Label(window, text= 'Enter something:')
lbl1.pack()

entry = Entry(window)
entry.pack()


button = Button(
    text="Click me!",
    command = lambda:print(entry.get())
)
button.pack()

window.mainloop()
````

The Button you define takes a function in as the command paramater in the definition of it.

In this case we define a lamda function to print out the data inside of the entry field using the .get() function of the entry field to retrieve the data.

## Rendering Pandas data

To render data from pandas in Tkinder we need to install a library, for that we'll use pip once again and install pandastable. In the command line:

\>pip install pandastable

Now that we have the needed libraries lets do a test UI where we render some of the sample data that comes with the library.

````python 
from tkinter import *
from pandastable import Table, TableModel

window = Tk()

window.title("Welcome to MyUI app")
window.geometry('850x600')

frame = Frame(window)
frame.pack(fill=BOTH,expand=1) 
table = Table(frame, dataframe=TableModel.getSampleData()) 
table.show() 

window.mainloop()
````

Now we have a window that displays a table with a tabel, in this window we used some new code that we've not seen before.

First we used frame, a Frame is a container that holds contents you can use frames to organise and space out your components. A frame can be used the same way as a Div in HTML.

Here we used the optional paramaters to fill the window with our frame.

Then we defined a Tabel and specified the contents of the tabel to be some sample data that came with pandastable.

We can use some more of the optional paramaters to expand the functionality of this Table, replace line 11 with:

````python 
table = Table(frame, dataframe=TableModel.getSampleData(),showtoolbar=True, showstatusbar=True) 
````

Now we have some extra GUI we can use to manipulate the Data we are displaying.

## Rendering Matplotlib 

Now that we have our Pandas data rendering code in place lets look at rendering MatPlotLib figures.

````python 
from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np

window = Tk()

window.title("Welcome to MyUI app")
window.geometry('850x600')

#Define a drawing function
fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

#Render the fucntion
canvas = FigureCanvasTkAgg(fig, master=window)  # A Tkinter.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


window.mainloop()
````

Here we imported something we havn't before, a backend rendering framework.

Basically this allows us to render matplotlib content on a Tkinter rendering backbone and thus insert matplotlib figures into our Tkinter GUIs. FigureCanvasTkAgg allows us to do exactly this, create canvases that can be packed or grided into a Tkinter Gui.

We also imported Matplotlib as well as numpy to generate our figures as normal.

We then go about generating our figure as normal and then using FigureCanvasTkAgg we generate a new TKinter renderable object that takes in the figure and a frame for refrence where to put it, in this case the whole window.

We then use the Draw function to Draw the Figure and ten the get_tk_widget().pack to first generate a widget that works with Tkinter and then to render the content inside of that widget.

## More complex Tkinter layouts

Now that we have both our advanced content types rendering lets look at making the app more "app-like" in functionality.

Lets prototype a simple app that has two Tabs that can switch content.

First we are gonna wrap all the rendering of functionality into their own functions.

````python
def DisplayPandasData(container,data): 
    f2 = Frame(container)
    f2.pack(fill=BOTH,expand=1) 
    table = Table(f2, dataframe=data,showtoolbar=False, showstatusbar=False) 
    table.show() 

def DrawMatplotlibFig(container,fig):
    canvas = FigureCanvasTkAgg(fig, master=container)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
 
````

We have a function that each takes in a Frame to contain the rendering of data. 