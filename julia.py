import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Parameters for the plot
im_width, im_height = 2000, 2000
c = complex(-0.2, 1)
zabs_max = 2    # escape threshold
nit_max = 1000
xmin, xmax = -2, 2
xwidth = xmax - xmin
ymin, ymax = -2, 2
yheight = ymax - ymin

julia = np.zeros((im_width, im_height))
for ix in range(im_width):
    for iy in range(im_height):
        nit = 0
        # Map pixel position to a point in the complex plane
        z = complex(ix / im_width * xwidth + xmin,
                    iy / im_height * yheight + ymin)
        # Apply Q_c to z repeatedly
        while abs(z) <= zabs_max and nit < nit_max:
            z = z**2 + c
            nit += 1
        shade = 1-np.sqrt(nit / nit_max)
        ratio = nit / nit_max
        julia[ix, iy] = ratio if nit < nit_max else 0

plt.pcolormesh(np.transpose(julia), cmap=cm.inferno)
plt.axis('equal')
plt.axis('off')
plt.show()
