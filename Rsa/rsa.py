# rozkodovani sifry RSA
from setting import *
from function import *

def main():

    # x = tajna zprava, n = zaklad, e = verejny exponent

    # z = x ^ d v Zm
    # z = (242 ** 11) % 2923

    # faktorizujeme n a spocteme eulerovu funkci n
    delitel = fermat(n)
    print "Delitel je",delitel
    delitel2 = n / delitel
    print "Druhy delitel je",delitel2
    euler_n = (delitel - 1) * (delitel2 - 1)
    print "Eulerova funkce je",euler_n

    # spocitame inverzi e v Z euler_n
    bezout = getBezout(euler_n,e)
    print "Inverze je",bezout

    # a tim zjistime soukromy klic
    d = bezout[2]#%euler_n
    print "Soukromy exponent je",d

    # takze muzeme desifrovat zpravu
    # z = x ^ d v Zm
    # z = (x**d)%n
    z = opakovanyCtverce(x,d,n)

    print "Ciselna zprava je",z
    print "Zprava je",ascii2txt(z)


# spustime main()
main()
