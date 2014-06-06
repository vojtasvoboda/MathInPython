# program pro vypocet determinantu
from numpy import *

# klic
klic = matrix([[18, 0,19,12,23],
               [22,30,32,19,10],
               [19,17, 2,32,32],
               [11,24,20,22, 5],
               [30, 0,19,26,22]])

A = matrix([[18, 0,19,12],
            [22,30,32,19],
            [19,17, 2,32],
            [11,24,20,22]])

det = linalg.det(A)

det = det * (1)

print det
print det%33
