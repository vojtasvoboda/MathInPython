# funkce implementujici Cinskou vetu o zbytcich
# main je dole

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

    # print " a | b | q | r | a2 | a1 | b2 | b1"
    # print " ",a," | ",b," | ",q," | ",r," | ",alfa2," | ",alfa1," | ",beta2," | ",beta1," "

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

        # print " ",a," | ",b," | ",q," | ",r," | ",alfa2," | ",alfa1," | ",beta2," | ",beta1
        a = b
        if (r != 0):
            b = r

    vysledek[0] = b
    vysledek[1] = alfa2
    vysledek[2] = beta2

    return vysledek

def main():
    
    # x = 9 v Z59
    # x = 18 v Z71
    # x = 8 v Z34
    # x = 29 v Z79
    # x = 19 v Z53

    # zde se nastavi hodnoty
    value = [9,18,8,29,19]
    # zde se nastavi zaklady cisel
    base  = [59,71,34,79,53]
    # vysledek vynulujeme
    results = [0,0,0,0,0]

    # x = 3 . ( 5 . 21 . y )
    index = 0
    for i in value:

        # 5 . 21 = 105
        bases = 1
        for j in base:
            bases = bases * j
        bases = bases / base[index]

        # 5 . 21 = 105 = 1 v Z4
        cisloMod = bases % base[index]

        # gcd(4,1) = 1 = 
        bezout = getBezout(cisloMod,base[index])

        if (bezout[1] < 0):
            bezout[1] = bezout[1] + base[index]
        print "Bezout",base[index],"je",bezout[1]

        results[index] = bezout[1] * bases * value[index]
        index = index + 1

    print results

    vysledek = 0
    for result in results:
        vysledek = vysledek + result

    zaklad = 1
    for mod in base:
        zaklad = zaklad * mod

    print "Cislo je",vysledek % zaklad,"v Z",zaklad

main()
    
