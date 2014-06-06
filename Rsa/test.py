from math import *
from function import *
from setting import *

# funkce pro vypocet faktorialu
def fact(x):
    return (1 if x==0 else x * fact(x-1))

# dalsi funkce pro faktorial
def factorial(n):
    sum = 1.0
    for m in range(1, int(n)+1):
        sum = float(m)*sum
    return sum

def pollard():

    n = 812423.0
    b = 26.0
    cislo = 2.0
    fact = factorial(b)
    a = opakovanyCtverce(cislo,fact,n)
    d = getGcd(a,n)
    print d

def odm():

    odm = sqrt(float(n))
    print odm


# spustime
odm()
