import numpy as np
from matplotlib import pyplot as plt


# xvalues = np.linspace(-2.25, 0.75, 1000)
# yvalues = np.linspace(-1.5, 1.5, 1000)
xvalues = np.linspace(-0.22, -0.21, 1000)
yvalues = np.linspace(-0.70, -0.69, 1000)
# size of these lists of x and y values
xlen = len(xvalues)
ylen = len(yvalues)

# mandelbrot function, takes the fixed parameter c and the maximum
# number of iterations maxiter, as inputs
def mandel(c, maxiter):
    # starting value of complex z is 0+0i before iterations update it
    z = complex(0,0)
    # iterating and stop when it's done maxiter times
    for iteration in range(maxiter):
        # main function which generates the output value of z
        # from the input values using the formula (z^2) + c
        z = (z*z) + c
        # if the (pythagorean) magnitude of the output complex
        # number z is bigger than 4, and if so stop iterating as we've diverged already
        if abs(z) > 4:
            break

    # return the number of iterations we actually did, not the final value of z, as this tells us how quickly the values diverged past the magnitude threshold of 4
    return iteration

# create an array of the right size to represent the atlas, we usethe number of items in xvalues and yvalues
atlas = np.empty((xlen,ylen))

# go through each point in this atlas array and test to see how many
# iterations are needed to diverge (or reach the maximum iterations when not diverging)

for ix in range(xlen):
    for iy in range(ylen):
        # at this point in the array, work out what the actual real
        # and imaginary parts of x are by looking it up in the xvalue and yvalue lists
        cx = xvalues[ix]
        cy = yvalues[iy]
        c = complex(cx, cy)
        # now we know what c is for this place in the atlas, 
        # apply the mandel() function to return the number of iterations it took to diverge
        # we use 40 maximum iterations to stop and accept the function didn't 
        atlas[ix,iy] = mandel(c,120)
        # atlas[ix,iy] = mandel(c,40)

# set the figure size
# figsize(18,18)
# plot the array atlas as an image, with its values represented as colours, peculiarity of python that we have to transpose the array

plt.imshow(atlas.T, interpolation="nearest")
plt.show()
