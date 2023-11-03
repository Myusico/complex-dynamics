import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Parameters for the plot
im_width, im_height = 3000, 2400
nit_max = 50
xmin, xmax = -2, 1
xwidth = xmax-xmin
ymin, ymax = -1.2, 1.2
yheight = ymax-ymin

mandelbrot = np.zeros((im_width, im_height))
for ix in range(im_width):
    for iy in range(im_height):
        nit = 0
        # Map pixel position to a point in the complex plane
        c = complex(ix/im_width*xwidth+xmin,
                    iy/im_height*yheight+ymin)
        z = 0
        # Apply Q_c to 0 repeatedly
        while abs(z) <= 2 and nit < nit_max:
            z = z**2+c
            nit += 1
        ratio = nit/nit_max
        mandelbrot[ix, iy] = ratio if nit < nit_max else 0

plt.pcolormesh(np.transpose(mandelbrot), cmap=cm.viridis)
plt.axis('equal')
plt.axis('off')
plt.show()
