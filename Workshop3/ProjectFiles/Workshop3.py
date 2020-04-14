import numpy as np
from pytictoc import TicToc
t = TicToc()

np.random.seed(0)

values = np.random.randint(1,100,size=1000000)

def calculate_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1/values[i]
    return output


#t.tic()
processed_values = calculate_reciprocals(values)
#t.toc('The loop took: ')

#t.tic()
processed_values = 1/values
#t.toc('Numpy took: ')

newarr = np.linspace(0,np.pi,5)

"""
print(newarr)
print(np.sin(newarr))
print(np.cos(newarr))
print(np.tan(newarr))

print(np.add.reduce(newarr))
print(np.add.accumulate(newarr))
"""
