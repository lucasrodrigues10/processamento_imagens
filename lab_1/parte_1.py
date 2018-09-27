import numpy as np
import pylab as pl
from matplotlib.colors import hsv_to_rgb

H = np.mgrid[0:1:300j]
S = np.ones_like(H)
V = S
HSV = np.dstack((H, S, V))
RGB = hsv_to_rgb(HSV)
pl.imshow(RGB, origin="lower", extent=[0, 360, 0, 1], aspect=150)
pl.xlabel("H")
pl.ylabel("V")
pl.show()
