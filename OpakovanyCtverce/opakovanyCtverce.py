# implementuje algoritmus opakovanych ctvercu

def main():

    cislo = 11
    exponent = 16601
    zaklad = 36181

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

    print "pole operaci je",pole
    vysledek = 1

    for flag in pole:
        if (flag == '0'):
            print "vysledek = ",vysledek,"*",cislo
            vysledek = vysledek * cislo
            print "mezivysledek",vysledek
        else:
            print "vysledek = ",vysledek,"^2"
            vysledek = vysledek ** 2
            print "mezivysledek",vysledek
        vysledek = vysledek % zaklad
        print "po modulu",vysledek
        print ""

    print cislo,"^",exponent,"=",vysledek,"v Z",zaklad

# spustime funkci main()
main()
