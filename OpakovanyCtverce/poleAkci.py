# funkce vraci pole akci pro algoritmus opakovanych ctvercu
def main():

    exp = 233
    pole = []

    while (exp > 1):
        if (exp % 2 == 1):
            exp = exp - 1
            pole[:0] = ['0']
        else:
            exp = exp / 2
            pole[:0] = ['1']

    print pole

# spustime
main()
