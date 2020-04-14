import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()


rainfall = pd.read_csv('Seattle2014.csv')['PRCP'].values
millimeters  = rainfall/10 # 1/10mm -> mm

#plt.hist(millimeters)
#plt.show()

print("Number days without rain: ",np.sum(millimeters == 0))
print("Number of days with rain: ",np.sum(millimeters != 0))
print("Number of days with more than 5mm of rain:", np.sum(millimeters>5))
print("Number of days with < 5mm of rain: ", np.sum((millimeters < 5)&(millimeters > 0)))

rainy = (millimeters>0)
days = np.arange(365)
summer = (days>172) & (days < 262)

print("Median of rain amount (mm): ",np.median(millimeters[rainy]))
print("Median of rain during summer(mm): ",np.median(millimeters[summer]))
print("Median of rain during nonsummer rainy days: ",np.median(millimeters[rainy & ~summer]))
print("Maximum amount of rain we got during summer:",np.max(millimeters[summer]))