#!/usr/bin/env python


from __future__ import division

import numpy as np
from matplotlib import pyplot as plt


def main():
    koeffs = [.3, 1.2, .1, 7]
    p = lambda x: koeffs[0] * x**3 + koeffs[1] * x**2 + koeffs[2] * x + koeffs[3]
    x = np.linspace(-5, 5, 100)
    y = p(x) + 2 * np.random.randn(100) - 1
    # fit
    fit =  np.polyfit(x, y, 3)
    p_fit = np.poly1d(fit)
    print "Real coefficients:", koeffs
    print "Fitted coefficients:", fit
    # plot
    plt.scatter(x, y)
    plt.plot(x, p_fit(x), 'orange', lw=2)
    plt.show()


if __name__ == '__main__':
    main()
