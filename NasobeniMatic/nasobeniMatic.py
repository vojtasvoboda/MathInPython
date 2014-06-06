# funkce implementujici nasobeni matic
from numpy import *

def main():

    A = matrix([[6,21,12,23,20],
                [7,7,11,0,20],
                [10,25,3,26,13],
                [1,25,3,1,25],
                [21,8,21,26,28]])

    i = 0
    for a in A:
        j = 0
        for aa in a:
            A[i][j] = (aa * 28) % 33
            j = j + 1
        i = i + 1

    print A

#spustime main
main()
