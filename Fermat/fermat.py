# implementace Fermatova faktorizacniho algoritmu
from setting import *
from math import sqrt

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

def fermat():

    n = 23360947609L
    t = intsqrt(n)
    print "t =",t

    odmocnina = sqrt( t**2 - n )
    print "odmocnina =",odmocnina
    odmocninaOkr = round(odmocnina)
    print "-" * 50

    while (odmocnina != odmocninaOkr):
        t = round(t + 1)
        odmocnina = sqrt( t**2 - n )
        odmocninaOkr = round(odmocnina)        
        print "t = ",t,"odm = ",odmocnina

    print "-" * 50
    a = t + odmocnina
    b = t - odmocnina
    print "a =",a
    print "b =",b

    c = a * b

    if (c == n): print "test ok"

def fermat2():

  t = intsqrt(n)
  i=0

  while(1==1):
    i=i+1
    a = t*t-n
    b = intsqrt(a) * intsqrt(a)
    print [i,t,a,b]
    if (a == b):
      print "probehla faktorizace "
      print  str(n)  +" = " + str(t-intsqrt(a)) +" * " + str(t+intsqrt(a))
      break;
    t=t+1
  l = t-intsqrt(a)
  m = t+intsqrt(a)
  o = n / l

  if (m == o): print "ok"

# spustime Fermata
fermat2()

