# zjisti nejvetsi spolecny nasobek dvou cisel

def getGcd(a,b):

    q = 0
    r = 1

    # 427 = 3.133 + 28
    #  a  = q. b  + r
    while (r != 0):
        r = a % b
        q = (a - r) / b
        print a, "=", q, "*", b, "+", r
        a = b
        if (r != 0):
            b = r

    return b

def main():

    a = 32 #427
    b = 23 #133
    gcd = getGcd(a,b) #7
    print "Vysledek je ",gcd

main()
