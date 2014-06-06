# vypocita Bezoutovu rovnost

def getBezout(a,b):

        q = 0
        r = 1
        alfa = 0
        alfa1 = 0
        alfa2 = 1
        beta = 0
        beta1 = 1
        beta2 = 0
        vysledek = [0,0,0]

        print " a | b | q | r | a2 | a1 | b2 | b1"
        print " ",a," | ",b," | ",q," | ",r," | ",alfa2," | ",alfa1," | ",beta2," | ",beta1," "

        # 427 = 3.133 + 28

        #  a  = q. b  + r
        # alfa1 = alfa2 - q * alfa1 

        while (r != 0):
            r = a % b
            q = (a - r) / b
            alfa = alfa2 - (q * alfa1)
            alfa2 = alfa1
            alfa1 = alfa
            beta = beta2 - (q * beta1)
            beta2 = beta1
            beta1 = beta

            print " ",a," | ",b," | ",q," | ",r," | ",alfa2," | ",alfa1," | ",beta2," | ",beta1
            a = b
            if (r != 0):
                b = r

        vysledek[0] = b
        vysledek[1] = alfa2
        vysledek[2] = beta2

        return vysledek


def main():

        prvni=3714019 #427
        druhy=33 #133
        delitel=getBezout(prvni,druhy) #7=5.427+(-16).133
        print "gcd(",prvni,",",druhy,") = ",delitel[0]," = (",delitel[1]," * ",prvni,") + (",delitel[2]," * ",druhy,")"

main()
