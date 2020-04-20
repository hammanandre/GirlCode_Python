import numpy as np 

name = ['Cat', 'mouse', 'Fluffy', 'Whiskers']
age = [5, 4, 11, 34]
weight = [12.0, 5.5, 23.0, 45.5]

dateformat = {'names':('name','age','weight'),'formats':('U10','i4','f8')}

x = np.zeros(4,dtype=dateformat)
#print(x)
#print(x.dtype)

x['name'] = name
x['age'] = age
x['weight'] = weight

print(x)

print(x['name'])

print(x[x['weight']>15]['name'])