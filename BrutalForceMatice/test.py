from numpy import *
from time import strftime, gmtime

def num_digits(n):
    count = 0
    while n:
        count = count+1
        n = n/10
    return count

def ascii2txt(zprava):

    text = ""
    while(zprava>0):
        znak = zprava%256
        text = text + chr(znak)
        zprava = zprava / 256

    return text

def main():

    matice = matrix([[1],[2],[3],[4],[5]])

    if ( (matice[0]==1) & (matice[1]==2) ):
        print "ahoj"

    print "ahoj",
    print(strftime("%H:%M:%S", gmtime()),"","")

    matice = matrix([[0],[0],[0],[0],[2]])

    klic = matrix([[18, 0,19,12,23],
                   [22,30,32,19,10],
                   [19,17, 2,32,32],
                   [11,24,20,22, 5],
                   [30, 0,19,26,22]])

    nasobek = klic * matice
    if ( (nasobek[0]%26==20) & (nasobek[1]==20) & (nasobek[2]==64) & (nasobek[3]==10) & (nasobek[4]==44)):
        print "je to ona"

    zprava = 158099617082024048411956288835831262368429199433185203960613617967859522074257661361171706497990759607576163901390292125693446450490811153451273725216546165407376264831832545934086L
    print "zprava je",ascii2txt(zprava)

def neco():

    zprava = 158099617082024048411956288835831262368429199433185203960613617967859522074257661361171706497990759607576163901390292125693446450490811153451273725216546165407376264831832545934086L

    while zprava > 1:
        zprava = zprava / 256
        print zprava

neco()

