# implementace Eratosthenova sita, ktery vraci prvocisla

def eratosthen():
    MaxN = 98                                                # horni hranice seznamu cisel
    SeznamN = range(2,MaxN+1)                                # vytvoreni seznamu cisel v rozpeti <2,1024>
    Prvocisla = []                                           # vytvoreni (prozatim) prazdneho seznam prvocisel
    while SeznamN[0]**2 <= SeznamN[-1]:                      # Dokud bude ctverec prvniho prvku SeznamuN mensi nebo roven poslednimu
                                                             # prvku SeznamuN, vykonej:
        Prvocisla.append(SeznamN[0])                         #    1)K seznamu Prvocisla pripoj prvni cislo ze SeznamuN
        Nasobky = range(SeznamN[0],SeznamN[-1]+1,SeznamN[0]) #    2)Vytvor seznam nasobku naposledy pripojeneho Prvocisla
        for k in Nasobky:                                    #    3)Pro kazde cislo "k" v seznamu Nasobky:
            if k in SeznamN:                                 #        1)Pouze pokud se k naleza v SeznamuN:
                SeznamN.remove(k)                            #            1)Odstran cislo/nasobek k ze SeznamuN;kod se opakuje od 4 radku
                                                             # Prvni cislo v seznamu je vetsi jak odmocnina z cisla posledniho a tedy
    Prvocisla.extend(SeznamN)                                # zbyla cisla jsou prvocisla. Extend je podobne k append.
    print Prvocisla                                          # Zobraz vysledek!

eratosthen()
