"""
This script uses the cplot function in mpmath to plot the Mandelbrot set.
By default, the fp context is used for speed. The mp context could be used
to improve accuracy at extremely high zoom levels.
"""

import mpmath
import cmath

ctx = mpmath.fp
# ctx = mpmath.mp

ITERATIONS = 200
POINTS = 16000000
ESCAPE_RADIUS = 8

# Full plot
r = float('-1.6259733936')
i = float('-0.0000011318')
RE = [r-2e-2, r+2e-2]
IM = [i-2e-2, i+2e-2]

# A pretty subplot
#RE = [-0.96, -0.80]
#IM = [-0.35, -0.2]


def mandelbrot(z):
    c = z
    for i in range(ITERATIONS):
        zprev = z
        z = z*z + c
        if abs(z) > ESCAPE_RADIUS:
            return ctx.exp(1j*(i + 1 - ctx.log(ctx.log(abs(z)))/ctx.log(2)))
    return 0

try:
    import psyco
    psyco.full()
except ImportError:
    pass

import cmath
import math
mapping = lambda i: (1 - math.atan(3*abs(i))/math.pi*2)*(cmath.phase(i)+math.pi)/(2*math.pi)

ctx.cplot(mandelbrot, RE, IM, points=POINTS, verbose=1, color=lambda i:
    (mapping(i), mapping(i), mapping(i)), file='fractal.png', dpi=4000)
