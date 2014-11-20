#!/usr/bin/env python
from sys import argv
from parallel import Parallel
p = Parallel()

args = argv[1:]
if args:
    if 'on' in args:
        p.setData(0)
    if 'off' in args:
        p.setData(255)
