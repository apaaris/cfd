# 1D Linear Convection

# Setup
import numpy
from matplotlib import pyplot
import time, sys

# Variables
cells = 41  # try changing this number from 41 to 81 and Run All ... what happens?
dx = 2 / (cells-1)
time_steps = 25
dt = .025
c = 1
u = numpy.ones(cells)

# Setting initial conditions
for i in range(int(0.5/dx), int(1/dx + 1)):
    u[i] = 2


un = numpy.ones(cells)
for n in range(time_steps):
    un = u.copy()
    for i in range(1,cells):
        u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
pyplot.plot(numpy.linspace(0, 2, cells), u)
pyplot.show()
