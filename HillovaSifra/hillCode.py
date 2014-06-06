# dekodovani Hillovy sifry
# reseni predchoziho prikladu: 00 10 02 11 00
from numpy import matrix
from numpy import linalg

def main():

    # zaklad zadani
    zaklad = 33
    # zprava
    zprava1 = matrix([[20],[17],[2],[5],[6]])
    # klic
    klic = matrix([[18, 0,19,12,23],
                   [22,30,32,19,10],
                   [19,17, 2,32,32],
                   [11,24,20,22, 5],
                   [30, 0,19,26,22]])
    # zprava
    zprava2 = matrix([28,9,8,4,14])

    # ------------------------------

    transponovana = matrix( [[ 3,27, 6,17,32],
                             [31,31,11, 0,32],
                             [16, 7,18, 2, 1],
                             [28, 7,18,28, 7],
                             [27,26,27, 2,25]])

    tr2 = matrix([[6,21,12,23,20],
                [7,7,11,0,20],
                [10,25,3,26,13],
                [1,25,3,1,25],
                [21,8,21,26,28]])    

    #   A  *  X   =   B
    #   X  = A(-1) *  B
    X = tr2 * zprava1
    print X

# spustime main
main()
