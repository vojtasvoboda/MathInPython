# funkce pro pocitani RSA
from math import *

# zjisti celociselneho delitele daneho cisla
# param: cislo pro ktery chceme zjistit prvociselny rozklad
# return: jednoho celociselneho delitele cisla n
def getDivider(n):

    odm = round(sqrt(float(n)))
    # najdeme pole prvocisel do odmocniny
    prvocisla = eratosthen(odm)
    for i in prvocisla:
        if (n%i == 0):
            return i
    return 0

# vrati pole prvku Bezoutovy rovnosti
# param: dve cisla pro ktery chceme Bezouta
# return: prvky Bezouta v poli [b,alfa2,beta2]
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

# vrati GCD
def getGcd(a,b):

    q = 0
    r = 1

    # 427 = 3.133 + 28
    #  a  = q. b  + r
    while (r != 0):
        r = a % b
        q = (a - r) / b
        # print a, "=", q, "*", b, "+", r
        a = b
        if (r != 0):
            b = r

    return b

# implementuje algoritmus opakovanych ctvercu
# param: cislo, jeho exponent a zaklad zbytkovy tridy
# return: cislo, ktery je kongruentni se zadanym
def opakovanyCtverce(cislo,exponent,zaklad):

    # zjistime binarni rozvoj
    pole = []
    exp = exponent

    while (exp > 0):
        if (exp % 2 == 1):
            exp = exp - 1
            pole[:0] = ['0']
        else:
            exp = exp / 2
            pole[:0] = ['1']

    print "start opakovanyCtverce"
    vysledek = 1

    for flag in pole:
        if (flag == '0'):
            vysledek = (vysledek * cislo)%zaklad
            print vysledek
        else:
            vysledek = (vysledek ** 2)%zaklad
            print vysledek

    return vysledek

# Fermatuv algoritmus
def fermat(n):

    t = intsqrt(n)
    i=0
    while(1==1):
        i=i+1
        a = t*t-n
        b = intsqrt(a) * intsqrt(a)
        if (a == b):
          break;
        t=t+1
    return t-intsqrt(a)

# celociselna odmocnina
def intsqrt(n):
    l = 1
    h = n
    while h - l > 1 :
        c = (l + h) / 2
        if c * c < n :
            l = c
        else :
            h = c
    return h

# prevod ciselny zpravy na text
# param: zakodovany text
# return: rozkodovany text
def ascii2txt(zprava):

    text = ""
    while(zprava>1):
        znak = zprava%256
        text = text + chr(znak)
        zprava = zprava / 256

    return text

# testovaci spousteni funkci
# opakovanyCtverce(11,233,373)
# print ascii2txt(1785686081)
print getBezout(35712,3989)
