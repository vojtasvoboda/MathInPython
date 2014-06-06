# skript pro vytvoreni inverzni matice a vynasobeni s jinou
# A . X = B; X = A-1 . B
# pouzivam knihovnu numpy
from numpy import matrix
from numpy import linalg

def main():

    # zakodovana zprava    
    zprava1 = matrix([[20],[17],[2],[5],[6]])
    # klic
    klic = matrix([[18, 0,19,12,23],
                   [22,30,32,19,10],
                   [19,17, 2,32,32],
                   [11,24,20,22, 5],
                   [30, 0,19,26,22]])

    # vytvorime matici algebraickych doplnku
    d = matrix([[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]])

    tmp = matrix([[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]])    

    i = 0
    j = 0

    # prochazime klic bez i-teho radku a j-teho sloupce
    # sebereme i-ty radek
    radek = 0
    for radky in klic:
        if (radek != i):
            tmp[radek] = klic[i]
        radek = radek + 1

    print tmp
        
    
#spustime main
main()
