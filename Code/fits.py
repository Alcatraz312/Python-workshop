from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

def load_fits(x):
    hdulist=fits.open(x)
    global data
    data=hdulist[0].data

    
    arg_max=np.argmax(data)
    max_pos=np.unravel_index(arg_max, data.shape)
    return max_pos

    

x=r"image"
print(load_fits(x))

plt.imshow(data, cmap=plt.cm.viridis)
plt.xlabel("X-pixels (RA)")
plt.ylabel("Y-pixels (Dec)")
plt.colorbar()
plt.show()