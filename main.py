# -*- coding: utf-8 -*-

import cmath
from math import trunc
import numpy
import cv2 as cv

goldenRatio = 89/55
C = complex(goldenRatio - 2, goldenRatio - 1 )
I = complex(0, 1)
rangeReal = [-1.5, 1.5]
rangeImag = [-1.5, 1.5]
imageshape = [1000, 1000]
maxIteration = 100
incrementReal = (rangeReal[1] - rangeReal[0] ) / imageshape[0]
incrementImag = (rangeImag[1] - rangeImag[0]) /  imageshape[1]
img = numpy.zeros(shape=[imageshape[1], imageshape[0], 3], dtype=numpy.uint8)
img[:,:] = [0, 0, 0]


def f(x):
    return x ** 2 + C

def tends2infinity(x):
    iteretion = 0
    for i in range(maxIteration, 0, -1):
        x = f(x)
        iteretion += 1
        if (abs(x) > rangeReal[1] or abs(x) > rangeImag[1]):
            return iteretion
    return False

for j in range(0, imageshape[1]):
    for r in range(0, imageshape[0]):
        newComplex = complex(rangeReal[0] + r * incrementReal, rangeImag[0] + j * incrementImag)
        iteretion = tends2infinity(newComplex)
        if (iteretion):
            img[j, r] = [10 + 2*iteretion, 250 - iteretion, 250]
      

dirname = "juliaSet_C=(" + str(round(C.real, 3)) + ")+(" + str(round(C.imag, 3))
dirname = dirname + "i)_q=" + str(maxIteration) + ".png"
if (cv.imwrite(dirname, img)):
    print("finished!")
else: print("error...")

