# program pro faktorizaci cisla
from setting import *
from math import *
from primes import *
import random

# importovali jsme promenny: x, n, e

def nejvetsi_spolecny_delitel(cislo1,cislo2):
    while cislo2 != 0:
        r=cislo1%cislo2
        cislo1=cislo2
        cislo2=r
    return cislo1

def f(x, n):      
    return (x**2+random.randint(1, n-1))%n

def pollard(n):
    a = random.randint(2, n-3)
    b = random.randint(1, n-1)
    g = 1
    while g == 1:
        a = f(a, n)
        b = f(b, n)
        b = f(b, n)
        g = nejvetsi_spolecny_delitel(abs(a-b), n)
    if g == n:
        return -1
    return g

def main():
    for prime in p:
        if (n%prime == 0):
            return prime

# spustime main
main()
