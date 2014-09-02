#!/usr/bin/env python

from __future__ import division

import numpy as np
from matplotlib import pyplot as plt



def main():
    f = lambda x: .3 * x**3 + 1.2 * x**2 + .1 * x + 7
    x = np.linspace(-2, 2, 100)
    y = f(x) + 2 * np.random.randn(100) - 1
    # fit
    fit =  np.polyfit(x, y, 3)
    p = np.poly1d(fit)
    # plot
    plt.scatter(x, y)
    plt.plot(x, p(x))
    plt.show()

if __name__ == '__main__':
    main()
