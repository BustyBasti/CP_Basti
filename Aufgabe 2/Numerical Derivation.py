from __future__ import division
__author__ = 'Sebastian'

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2


def fprime(x):
    return 2*x


class Function(object):
    def __init__(self, function):
        self.defn = function

    def forward(self, x_0, h):
        return (self.defn(x_0 + h) - self.defn(x_0))/h

    def central(self, x_0, h):
        return (self.defn(x_0 + h/2) - self.defn(x_0 - h/2))/h

    def extrapolate(self, x_0, h):
        return (8 * (self.defn(x_0 + h/4) - self.defn(x_0 - h/4)) -\
               (self.defn(x_0 + h/2) - self.defn(x_0 - h/2)))/(3 * h)


F = Function(f)

h_list = 10**(np.linspace(-10.0, 0.0, 10, endpoint=False))
error_forward = []
error_central = []
error_extrapolate = []
fprimelist = []

for z in h_list:
    error_central.append(abs(fprime(2) - F.central(2, z)))
    fprimelist.append(F.central(2, z))

print np.linspace(-10, 0, 10, endpoint=False)
print h_list
print fprime(2)
print fprimelist
print error_central


plt.plot(h_list, error_central, c='r')
plt.subplot(111, yscale='log', xscale='log')
plt.xlim(10**(-10), 10**(-1))
plt.ylim(10**(-18), 10**(-6))
plt.show()