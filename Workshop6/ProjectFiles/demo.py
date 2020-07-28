from tkinter import *
from tkinter import ttk

from pandastable import Table, TableModel

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np

def DisplayPandasData(container,data): 
    f2 = Frame(container)
    f2.pack(fill=BOTH,expand=1) 
    table = Table(f2, dataframe=data,showtoolbar=False, showstatusbar=False) 
    table.show() 

def DrawMatplotlibFig(container,fig):
    canvas = FigureCanvasTkAgg(fig, master=container)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

window = Tk()
window.title("Welcome to MyUI app")
window.geometry('850x600')

window.mainloop()