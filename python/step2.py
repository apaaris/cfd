# Nonlinear Convection

# Setup

import numpy    
from matplotlib import pyplot

cells = 41
dx = 2 / (cells - 1)
time_steps = 20    
dt = .025  #dt is the amoutime_steps of time each timestep covers (delta t)

u = numpy.ones(cells)      #as before, we initialize u with every value equal to 1.
u[int(.5 / dx) : int(1 / dx + 1)] = 2  #then set u = 2 between 0.5 and 1 as per our I.C.s

un = numpy.ones(cells) #initialize our placeholder array un, to hold the time-stepped solution

for n in range(time_steps):  #iterate through time
    un = u.copy() ##copy the existing values of u itime_stepso un
    for i in range(1, cells):  ##now we'tll iterate through the u array

     ###This is the line from Step 1, copied exactly.  Edit it for our new equation.
     ###then uncommetime_steps it and run the cell to evaluate Step 2

           u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1])


pyplot.plot(numpy.linspace(0, 2, cells), u) ##Plot the results
pyplot.show()
