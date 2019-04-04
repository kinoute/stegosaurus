# works in Jupyter

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,12,10)
y = np.sin(x)

plt.plot(x,y)
