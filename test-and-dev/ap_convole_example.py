import matplotlib.pyplot as plt
import astropy
import numpy as np
from astropy.convolution import convolve as ap_convole
from astropy.convolution import Box2DKernel

nx=30;ny=30;
a=np.random.normal(size=(nx,ny))
plt.plot(a.flatten())
plt.show()

b2dk=Box2DKernel(9)
ac=ap_convole(a,b2dk)
plt.plot(ac.flatten())
plt.show()
