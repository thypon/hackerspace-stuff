#!/usr/bin/env python3

from sys import argv
from sh import espeak
from time import sleep


def pi_digits():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = (10*q, 10*(r-m*t), t, k,
                                (10*(3*q+r))//t - 10*m, x)
        else:
            q, r, t, k, m, x = (q*k, (2*q+r)*x, t*x,
                                k+1, (q*(7*k+2)+r*x)//(t*x), x+2)


try:
    for digit in pi_digits():
        print(digit)
        espeak(digit)
        sleep(float(argv[1]) if argv[1:] else 1)
except KeyboardInterrupt:
    pass
