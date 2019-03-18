#!/usr/bin/env python

# this script is for calculation of visual angle
# example readT.py 0.67 136 3
# written by Uksu, Choi (uschoi@nict.go.jp)

import sys
from math import exp, expm1
import math
from decimal import *
# getcontext().prec = 2

echo_spacing = float(sys.argv[1])
EPI_factor = float(sys.argv[2])
iPAT = float(sys.argv[3])

readoutT = (((EPI_factor-1)*echo_spacing/iPAT))/1000


print '[Readout Time] =',"{0:.4f}".format(readoutT), 'second'
