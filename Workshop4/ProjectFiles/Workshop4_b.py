import numpy as np 

x = np.arange(12).reshape((3,4))
print(x)

x_view = x[:2,:2]
print(x_view)

x_view[0,0] = 12

print(x_view)

print(x)

x_copy = x[:2,:2].copy()