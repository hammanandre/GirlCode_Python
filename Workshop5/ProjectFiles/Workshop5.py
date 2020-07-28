import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter

data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}

Keys = list(data.keys())
values = list(data.values())

def currencyformatter(x, pos):
    if x>=1e6:
        s = 'R{:1.1f}M'.format(x*1e-6)
    else :
        s = 'R{:1.0f}K'.format(x*1e-3)
    return s

formatter = FuncFormatter(currencyformatter)

companies_Mean = np.mean(values)

plt.rcParams.update({"figure.autolayout":True})
fig,ax= plt.subplots()
plt.style.use("fivethirtyeight")

ax.barh(Keys,values)
ax.set(ylabel='Companies',xlabel='Annual Revenue',title='Companies Annual Revenue')

labels = ax.get_xticklabels()

plt.setp(labels,horizontalalignment='right',rotation=45)

ax.axvline(companies_Mean,ls='--',color='r')
ax.xaxis.set_major_formatter(formatter)
ax.set_xticks([0,25e3,50e3,75e3,100e3,125e3])

for group in [3,5,8]:
    ax.text(145000,group,"New annotation",fontsize = 10, verticalalignment = "center")

plt.show()


