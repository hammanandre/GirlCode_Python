import numpy as np 

x = np.arange(0,10)
print(x)
print(x.shape)

x2 = np.linspace(1,10,10)
#print(x2)

print("single index ",x[0])
print("Reverse index ",x[-1])

ind = [2,4,5]
print("List of indexes ",x[ind])

ind = np.array([[4,1],[1,7]])
print("multi-dim indexes ", x[ind])

#x[start:stop:step]
#x[0:size of the collection:1]

print("First five elements ",x[:5])
print("First five elements ",x[5:])
print("Middle values ",x[4:7])
print("Every second value ",x[::2])

print("Inversed ",x[::-1])
