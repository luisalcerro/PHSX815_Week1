
import numpy as np
import matplotlib.pyplot as plt
# import data.txt
filename = 'data.txt'
dat = np.loadtxt(filename)

# creates histogram
n, bins, patches = plt.hist(dat, 50, density=True, facecolor='g', alpha=1.0)

# plot formating options
plt.xlabel('x')
plt.ylabel('PROBABILITY')
plt.title('Plot of the data in data.txt file')
plt.grid(False)

# show figure (program only ends once closed
plt.show()
