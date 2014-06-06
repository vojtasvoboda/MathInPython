# mame zadanou zakodovanou zpravu a klic
# klic * x = zakodovana_zprava
# pomoci brutal force hledam x

from numpy import *
from time import strftime, gmtime

def main():

    # zprava
    zprava = matrix([[20],[17],[2],[5],[6]])
    # klic
    klic = matrix([[18, 0,19,12,23],
                   [22,30,32,19,10],
                   [19,17, 2,32,32],
                   [11,24,20,22, 5],
                   [30, 0,19,26,22]])

    print "Brutal force started in",strftime("%H:%M:%S", gmtime())

    for a in range(26):
        print ""
        print a,
        for b in range(26):
            print ".",
            for c in range(26):
                for d in range(26):
                    for e in range(26):
                        matice = matrix([[a],[b],[c],[d],[e]])
                        nasobek = klic * matice
                        if ( (nasobek[0]%33==28) & (nasobek[1]%33==9) & (nasobek[2]%33==8) & (nasobek[3]%33==4) & (nasobek[4]%33==14)):
                            print matice

    print ""
    print "Brutal force ended in",strftime("%H:%M:%S", gmtime())                            


# spustime main()
main()
