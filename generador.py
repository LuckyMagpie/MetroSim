from sys import argv

def mcl(semilla, cantidad):
    lst = []
    for v in xrange(cantidad):
        R = (1664525.0 * semilla + 1013904223.0) % 4294967296.0
        semilla = R
        R /= 4294967296
        lst.append(R)
    return lst

def mcm(semilla, cantidad):
    lst = []
    for v in xrange(cantidad):
        R = 16807.0 * semilla % 2147483647.0
        semilla = R
        R /= 2147483647
        lst.append(R)
    return lst

